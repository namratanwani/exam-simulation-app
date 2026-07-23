"""SQLite persistence for web-UI quiz attempts, so past quizzes (with their
score and any missed questions) can be reviewed later from the "Wrong
Answers" page, grouped one expander per attempt.
"""

import json
import os
import sqlite3
from datetime import datetime
from pathlib import Path

# Overridable via QUIZ_DB_PATH (e.g. for testing against a throwaway file
# instead of the user's real quiz history).
DB_PATH = Path(os.environ.get("QUIZ_DB_PATH", Path(__file__).resolve().parent.parent / "wrong_answers.db"))


def _connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = _connect()
    existing_cols = {
        r["name"] for r in conn.execute("PRAGMA table_info(wrong_answers)")
    }
    if existing_cols and "attempt_id" not in existing_cols:
        # Older schema (single flat table, no per-attempt grouping) — replaced
        # by the attempts/wrong_answers pair below.
        conn.execute("DROP TABLE IF EXISTS wrong_answers")
        conn.execute("DROP TABLE IF EXISTS attempts")

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            label TEXT NOT NULL,
            taken_at TEXT NOT NULL,
            score REAL NOT NULL,
            total INTEGER NOT NULL,
            pct INTEGER NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS wrong_answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            attempt_id INTEGER NOT NULL REFERENCES attempts(id),
            source TEXT NOT NULL,
            stem TEXT NOT NULL,
            path TEXT, module TEXT, section TEXT,
            stem_html TEXT, options_html TEXT, sequence TEXT,
            correct_answer TEXT, given_answer TEXT,
            explanation_html TEXT, status TEXT, fraction REAL
        )
        """
    )
    old_schema = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='in_progress'"
    ).fetchone()
    if old_schema and "CHECK" in old_schema["sql"]:
        # Older schema only ever tracked a single singleton row (id fixed to
        # 1 via a CHECK constraint) — replaced by a normal auto-incrementing
        # table so multiple unfinished quizzes can be tracked independently.
        conn.execute("DROP TABLE IF EXISTS in_progress")

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS in_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            label TEXT NOT NULL,
            question_ids TEXT NOT NULL,
            answers TEXT NOT NULL,
            shuffle_seed INTEGER NOT NULL,
            started_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def save_progress(progress_id, label, question_ids, answers, shuffle_seed):
    """Insert (progress_id is None) or update (progress_id is an existing
    row's id) one in-progress quiz. Returns the row's id either way, so
    callers can stash it in the session for subsequent saves.

    Each quiz you start-but-don't-finish gets its own row, so several can be
    resumed independently later — this survives closing the browser or
    restarting the server overnight, since it isn't tied to the session
    cookie."""
    conn = _connect()
    now = datetime.now().isoformat()
    if progress_id is not None:
        cur = conn.execute(
            """UPDATE in_progress SET label=?, question_ids=?, answers=?, shuffle_seed=?, updated_at=?
               WHERE id=?""",
            (label, json.dumps(question_ids), json.dumps(answers), shuffle_seed, now, progress_id),
        )
        if cur.rowcount == 0:
            progress_id = None  # row was deleted/never existed — fall through to insert
    if progress_id is None:
        cur = conn.execute(
            """INSERT INTO in_progress (label, question_ids, answers, shuffle_seed, started_at, updated_at)
               VALUES (?,?,?,?,?,?)""",
            (label, json.dumps(question_ids), json.dumps(answers), shuffle_seed, now, now),
        )
        progress_id = cur.lastrowid
    conn.commit()
    conn.close()
    return progress_id


def get_progress(progress_id):
    """One in-progress quiz by id, with question_ids/answers decoded — or
    None if it doesn't exist (already finished/discarded)."""
    conn = _connect()
    row = conn.execute("SELECT * FROM in_progress WHERE id = ?", (progress_id,)).fetchone()
    conn.close()
    if not row:
        return None
    item = dict(row)
    item["question_ids"] = json.loads(item["question_ids"])
    item["answers"] = json.loads(item["answers"])
    return item


def list_progress():
    """All in-progress quizzes, most recently updated first."""
    conn = _connect()
    rows = conn.execute("SELECT * FROM in_progress ORDER BY updated_at DESC").fetchall()
    conn.close()
    result = []
    for row in rows:
        item = dict(row)
        item["question_ids"] = json.loads(item["question_ids"])
        item["answers"] = json.loads(item["answers"])
        result.append(item)
    return result


def delete_progress(progress_id):
    conn = _connect()
    conn.execute("DELETE FROM in_progress WHERE id = ?", (progress_id,))
    conn.commit()
    conn.close()


def record_attempt(label, score, total, pct, missed):
    """Insert one attempt row (always, even for a perfect score) plus a
    wrong_answers row for each missed question. Returns the new attempt id.

    missed: the same list results() builds — each item is
    {"q": enriched-question-dict, "given": [...], "fraction": f, "status": s}.
    """
    conn = _connect()
    now = datetime.now().isoformat()
    cur = conn.execute(
        "INSERT INTO attempts (label, taken_at, score, total, pct) VALUES (?,?,?,?,?)",
        (label, now, score, total, pct),
    )
    attempt_id = cur.lastrowid
    if missed:
        conn.executemany(
            """INSERT INTO wrong_answers
               (attempt_id, source, stem, path, module, section, stem_html, options_html, sequence,
                correct_answer, given_answer, explanation_html, status, fraction)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            [
                (
                    attempt_id,
                    m["q"]["source"], m["q"]["stem"], m["q"]["path"], m["q"]["module"], m["q"]["section"],
                    m["q"]["stem_html"], json.dumps(m["q"]["options_html"]),
                    json.dumps(m["q"]["sequence"]) if m["q"].get("sequence") else None,
                    json.dumps(m["q"]["answer"]), json.dumps(m["given"]),
                    m["q"]["explanation_html"], m["status"], m["fraction"],
                )
                for m in missed
            ],
        )
    conn.commit()
    conn.close()
    return attempt_id


def list_attempts():
    """All attempts, most recent first, each with its list of wrong
    questions under "questions" (not "items" — that name collides with
    dict.items() under Jinja's attribute-access syntax)."""
    conn = _connect()
    attempts = conn.execute("SELECT * FROM attempts ORDER BY taken_at DESC").fetchall()
    result = []
    for a in attempts:
        rows = conn.execute(
            "SELECT * FROM wrong_answers WHERE attempt_id = ? ORDER BY id", (a["id"],)
        ).fetchall()
        questions = []
        for row in rows:
            item = dict(row)
            item["options_html"] = json.loads(item["options_html"])
            item["sequence"] = json.loads(item["sequence"]) if item["sequence"] else None
            item["correct_answer"] = json.loads(item["correct_answer"])
            item["given_answer"] = json.loads(item["given_answer"])
            questions.append(item)
        result.append({**dict(a), "questions": questions})
    conn.close()
    return result


def clear_all():
    conn = _connect()
    conn.execute("DELETE FROM wrong_answers")
    conn.execute("DELETE FROM attempts")
    conn.commit()
    conn.close()

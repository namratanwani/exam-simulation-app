"""SQLite persistence for web-UI quiz attempts, so past quizzes (with their
score and any missed questions) can be reviewed later from the "Wrong
Answers" page, grouped one expander per attempt.
"""

import json
import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "wrong_answers.db"


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

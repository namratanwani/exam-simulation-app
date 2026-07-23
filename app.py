#!/usr/bin/env python3
"""AI-103 exam simulator — local web UI.

Same question bank and quiz logic as scripts/quiz.py, served as a small
Flask app so it can be used in a browser instead of the terminal.
"""

import html
import os
import random
import re
import sys
from pathlib import Path

from flask import Flask, redirect, render_template, request, session, url_for

sys.path.insert(0, str(Path(__file__).resolve().parent / "scripts"))
import history  # noqa: E402
from question_bank import (  # noqa: E402
    build_structure, load_bank, parse_sequence, random_letter_map, remap_options, score_answer,
)

app = Flask(__name__)
app.secret_key = os.environ.get("QUIZ_SECRET_KEY", os.urandom(24))
# Jinja's `tojson` filter hardcodes sort_keys=True via its own policy dict
# (independent of app.json.sort_keys) — override it so the module/section
# picker in index.html keeps study order instead of alphabetizing.
app.jinja_env.policies["json.dumps_kwargs"] = {"sort_keys": False}

BANK = load_bank()
STRUCTURE = build_structure(BANK)
history.init_db()

FENCE_RE = re.compile(r"```(\w*)\n(.*?)```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")


def render_md(text: str) -> str:
    """Minimal, safe markdown-ish rendering: escape, then re-add fenced/inline
    code and line breaks. Good enough for the question bank's own formatting."""
    escaped = html.escape(text)
    escaped = FENCE_RE.sub(lambda m: f'<pre class="code"><code>{m.group(2)}</code></pre>', escaped)
    escaped = INLINE_CODE_RE.sub(r"<code>\1</code>", escaped)
    escaped = escaped.replace("\n", "<br>")
    return escaped


def get_question_with_seed(idx: int, seed: int) -> dict:
    """BANK[idx] with its options relettered using an explicit seed — used
    when reconstructing a quiz that isn't the current session's (e.g. a
    different in-progress quiz shown on the Wrong Answers page)."""
    q = BANK[idx]
    mapping = random_letter_map(q, random.Random((seed, idx)))
    return remap_options(q, mapping)


def get_question(idx: int) -> dict:
    """BANK[idx] relettered using the current session's shuffle seed, so the
    same question shows the same shuffled letters across the GET (show) ->
    POST (grade) -> results (review) lifecycle of one quiz, but a fresh
    random arrangement each time a new quiz is started."""
    return get_question_with_seed(idx, session.get("shuffle_seed", 0))


def enrich(q: dict) -> dict:
    """Return a copy of q with pre-rendered HTML fields for templates."""
    seq = parse_sequence(q)
    sequence = None
    if seq:
        sequence = {
            # NB: key is "steps", not "items" — a dict key named "items" would
            # collide with dict.items() under Jinja's attribute-access syntax.
            "steps": [{"num": n, "text_html": render_md(text)} for n, text in seq["items"]],
            "correct_order": seq["correct_order"],
        }
    return {
        **q,
        "stem_html": render_md(q["stem"]),
        "options_html": {letter: render_md(text) for letter, text in q["options"].items()},
        "explanation_html": render_md(q["explanation"]) if q["explanation"] else "",
        "sequence": sequence,
    }


@app.route("/")
def index():
    session.pop("question_ids", None)
    session.pop("answers", None)
    session.pop("label", None)
    session.pop("recorded", None)
    session.pop("progress_id", None)
    return render_template(
        "index.html", structure=STRUCTURE, total=len(BANK),
        unfinished_count=len(history.list_progress()),
    )


@app.route("/start", methods=["POST"])
def start():
    mode = request.form.get("mode", "full")
    path = request.form.get("path", "")
    module = request.form.get("module", "")
    section = request.form.get("section", "")

    if mode == "full":
        pool_ids = list(range(len(BANK)))
        label = "Full exam"
    elif mode == "module":
        pool_ids = [i for i, q in enumerate(BANK) if q["path"] == path and q["module"] == module]
        label = f"{path} / {module}"
    else:  # section
        pool_ids = [
            i for i, q in enumerate(BANK)
            if q["path"] == path and q["module"] == module and q["section"] == section
        ]
        label = f"{path} / {module} / {section}"

    if not pool_ids:
        return render_template(
            "index.html", structure=STRUCTURE, total=len(BANK),
            error="No questions found for that selection.",
        )

    try:
        requested = int(request.form.get("count", 10))
    except ValueError:
        requested = 10
    n = max(1, min(requested, len(pool_ids)))

    session["question_ids"] = random.sample(pool_ids, n)
    session["answers"] = []
    session["label"] = label
    session["shuffle_seed"] = random.randint(0, 2**31 - 1)
    session.pop("recorded", None)
    session["progress_id"] = history.save_progress(
        None, label, session["question_ids"], session["answers"], session["shuffle_seed"],
    )
    return redirect(url_for("quiz"))


@app.route("/resume")
def resume_list():
    return render_template("resume.html", tests=history.list_progress())


@app.route("/resume/<int:progress_id>")
def resume_test(progress_id):
    progress = history.get_progress(progress_id)
    if not progress:
        return redirect(url_for("resume_list"))
    session["question_ids"] = progress["question_ids"]
    session["answers"] = progress["answers"]
    session["label"] = progress["label"]
    session["shuffle_seed"] = progress["shuffle_seed"]
    session["progress_id"] = progress["id"]
    session.pop("recorded", None)
    return redirect(url_for("quiz"))


@app.route("/resume/<int:progress_id>/discard", methods=["POST"])
def resume_discard(progress_id):
    history.delete_progress(progress_id)
    if session.get("progress_id") == progress_id:
        session.pop("question_ids", None)
        session.pop("answers", None)
        session.pop("label", None)
        session.pop("progress_id", None)
    return redirect(url_for("resume_list"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    ids = session.get("question_ids")
    if not ids:
        return redirect(url_for("index"))

    answers = session.get("answers", [])
    answered = len(answers)

    if request.method == "POST":
        if answered >= len(ids):
            return redirect(url_for("results"))
        q = get_question(ids[answered])
        if parse_sequence(q):
            given = [int(x) for x in request.form.getlist("order") if x.lstrip("-").isdigit()]
        else:
            given = request.form.getlist("letter")
        fraction, status = score_answer(q, given)
        answers = answers + [{"given": given, "fraction": fraction, "status": status}]
        session["answers"] = answers
        session["progress_id"] = history.save_progress(
            session.get("progress_id"), session["label"], session["question_ids"], answers, session["shuffle_seed"],
        )
        return render_template(
            "feedback.html",
            q=enrich(q),
            given=given,
            fraction=fraction,
            status=status,
            progress=answered + 1,
            total=len(ids),
            is_last=(answered + 1) >= len(ids),
            label=session.get("label", ""),
        )

    if answered >= len(ids):
        return redirect(url_for("results"))

    q = get_question(ids[answered])
    return render_template(
        "quiz.html",
        q=enrich(q),
        progress=answered + 1,
        total=len(ids),
        multi=len(q["answer"]) > 1,
        label=session.get("label", ""),
    )


@app.route("/results")
def results():
    ids = session.get("question_ids")
    answers = session.get("answers", [])
    if not ids or len(answers) < len(ids):
        return redirect(url_for("index"))

    total = len(ids)
    score = sum(a["fraction"] for a in answers)
    pct = round(100 * score / total) if total else 0

    missed = [
        {"q": enrich(get_question(idx)), "given": a["given"], "fraction": a["fraction"], "status": a["status"]}
        for idx, a in zip(ids, answers)
        if a["status"] != "correct"
    ]

    if not session.get("recorded"):
        history.record_attempt(session.get("label", ""), score, total, pct, missed)
        if session.get("progress_id") is not None:
            history.delete_progress(session["progress_id"])
            session.pop("progress_id", None)
        session["recorded"] = True

    return render_template(
        "results.html",
        score=score, total=total, pct=pct,
        missed=missed, label=session.get("label", ""),
    )


def _attempt_entry(a):
    return {
        "sort_key": a["taken_at"], "date": a["taken_at"][:10], "label": a["label"],
        "score_label": f"{a['score']:.1f}/{a['total']} ({a['pct']}%)",
        "extra": None, "resume_id": None, "questions": a["questions"],
    }


def _progress_entry(p):
    """A not-yet-finished quiz shown the same way as a completed attempt,
    with wrong answers computed from however much has been answered so far
    — so you don't have to finish a 100-question quiz to see how you're
    doing on the questions you've already answered."""
    answered = p["answers"]
    done = len(answered)
    score = sum(x["fraction"] for x in answered)
    pct = round(100 * score / done) if done else 0
    wrong = []
    for idx, ans in zip(p["question_ids"], answered):
        if ans["status"] == "correct":
            continue
        q = enrich(get_question_with_seed(idx, p["shuffle_seed"]))
        wrong.append({
            "path": q["path"], "module": q["module"], "section": q["section"],
            "stem_html": q["stem_html"], "options_html": q["options_html"],
            "sequence": q["sequence"], "explanation_html": q["explanation_html"],
            "correct_answer": q["answer"], "given_answer": ans["given"],
            "status": ans["status"], "fraction": ans["fraction"],
        })
    return {
        "sort_key": p["updated_at"], "date": p["updated_at"][:10], "label": p["label"],
        "score_label": f"{score:.1f}/{done} ({pct}%)" if done else "Not started yet",
        "extra": f"In progress — {done}/{len(p['question_ids'])} answered",
        "resume_id": p["id"], "questions": wrong,
    }


@app.route("/wrong-answers")
def wrong_answers():
    entries = [_progress_entry(p) for p in history.list_progress()]
    entries += [_attempt_entry(a) for a in history.list_attempts()]
    entries.sort(key=lambda e: e["sort_key"], reverse=True)
    return render_template("wrong_answers.html", entries=entries)


@app.route("/wrong-answers/clear", methods=["POST"])
def wrong_answers_clear():
    history.clear_all()
    return redirect(url_for("wrong_answers"))


if __name__ == "__main__":
    print(f"Loaded {len(BANK)} questions. Starting server at http://127.0.0.1:5050")
    app.run(host="127.0.0.1", port=5050, debug=True)

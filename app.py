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


def get_question(idx: int) -> dict:
    """BANK[idx] with its options relettered using a seed stored in the
    session, so the same question shows the same shuffled letters across the
    GET (show) -> POST (grade) -> results (review) lifecycle of one quiz,
    but a fresh random arrangement each time a new quiz is started."""
    q = BANK[idx]
    seed = session.get("shuffle_seed", 0)
    mapping = random_letter_map(q, random.Random((seed, idx)))
    return remap_options(q, mapping)


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
    return render_template("index.html", structure=STRUCTURE, total=len(BANK))


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
    return redirect(url_for("quiz"))


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

    return render_template(
        "results.html",
        score=score, total=total, pct=pct,
        missed=missed, label=session.get("label", ""),
    )


if __name__ == "__main__":
    print(f"Loaded {len(BANK)} questions. Starting server at http://127.0.0.1:5050")
    app.run(host="127.0.0.1", port=5050, debug=True)

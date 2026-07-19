"""Shared parser for modules/*/*/questions.md — used by both the CLI quiz
(quiz.py) and the web UI (app.py) so they stay in sync on one source of truth.
"""

import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES_DIR = ROOT / "modules"

QUESTION_RE = re.compile(
    r"\*\*Q(\d+)\.[^*\n]*\*\*\s*(?s:(.*?))\s*"
    r"((?:^[A-F]\.\s.*\n?)+)"
    r"(?s:.*?)\*\*Answer:\*\*\s*([A-F](?:\s*,\s*[A-F])*)\s*(?:[—-]\s*(.*))?",
    re.MULTILINE,
)
OPTION_RE = re.compile(r"^([A-F])\.\s(.*)$", re.MULTILINE)
SECTION_RE = re.compile(r"^##\s+(.*)$", re.MULTILINE)


ACRONYMS = ["AI", "MCP", "IQ", "A2A", "SDK", "API", "CI", "CD", "OCR", "RAG"]


def prettify(slug: str) -> str:
    slug = re.sub(r"^\d+-", "", slug)
    title = slug.replace("-", " ").title()
    for acronym in ACRONYMS:
        title = re.sub(rf"\b{acronym.title()}\b", acronym, title)
    return title


def parse_questions_file(path: Path, path_name: str, module_name: str):
    text = path.read_text(encoding="utf-8")

    # Map each character offset to the section heading active at that point.
    sections = [(m.start(), m.group(1).strip()) for m in SECTION_RE.finditer(text)]

    def section_at(offset):
        current = "General"
        for start, name in sections:
            if start <= offset:
                current = name
            else:
                break
        return current

    questions = []
    for m in QUESTION_RE.finditer(text):
        qnum, stem, options_block, answer_letters, explanation = m.groups()
        options = {letter: opt.strip() for letter, opt in OPTION_RE.findall(options_block)}
        answer = [a.strip() for a in answer_letters.split(",")]
        questions.append(
            {
                "path": path_name,
                "module": module_name,
                "section": section_at(m.start()),
                "stem": stem.strip(),
                "options": options,
                "answer": answer,
                "explanation": (explanation or "").strip(),
                "source": str(path.relative_to(ROOT)),
            }
        )
    return questions


def load_bank():
    bank = []
    for path_dir in sorted(MODULES_DIR.iterdir()):
        if not path_dir.is_dir():
            continue
        path_name = prettify(path_dir.name)
        for module_dir in sorted(path_dir.iterdir()):
            qfile = module_dir / "questions.md"
            if not qfile.is_file():
                continue
            module_name = prettify(module_dir.name)
            bank.extend(parse_questions_file(qfile, path_name, module_name))
    return bank


def build_structure(bank):
    """path -> module -> [section, ...] (in first-seen order), for UI pickers."""
    structure = {}
    for q in bank:
        modules = structure.setdefault(q["path"], {})
        sections = modules.setdefault(q["module"], [])
        if q["section"] not in sections:
            sections.append(q["section"])
    return structure


# --- "Build List / Sequence" questions -------------------------------------
# A handful of questions in the bank are step-ordering questions whose
# 4 options are pre-computed permutations of numbered steps (e.g. options
# "A. 3, 1, 5, 4, 2", "B. 1, 3, 5, 4, 2", ...). We detect those and render
# them as a real reorderable list instead of plain multiple choice.

SEQUENCE_OPTION_RE = re.compile(r"^\d+(\s*,\s*\d+){2,}$")
STEM_NUMBERED_LINE_RE = re.compile(r"^(\d+)\.\s+(.+)$", re.MULTILINE)
STEM_INLINE_PAREN_RE = re.compile(r"\((\d+)\)\s*([^,]+?)(?=,\s*\(\d+\)|\.\s*$|$)")


def parse_sequence(q: dict):
    """Return {"items": [(n, text), ...], "correct_order": [n, ...]} if q is
    a step-ordering question, else None."""
    if not q["options"] or not all(
        SEQUENCE_OPTION_RE.match(opt.strip()) for opt in q["options"].values()
    ):
        return None

    items = STEM_NUMBERED_LINE_RE.findall(q["stem"])
    if len(items) < 2:
        items = STEM_INLINE_PAREN_RE.findall(q["stem"])
    if len(items) < 2:
        return None

    items = [(int(n), text.strip().rstrip(".").strip()) for n, text in items]
    items.sort(key=lambda x: x[0])

    correct_letter = q["answer"][0]
    correct_order = [int(x) for x in re.split(r"\s*,\s*", q["options"][correct_letter].strip())]

    if sorted(correct_order) != [n for n, _ in items]:
        return None  # sanity check failed — don't treat as a sequence question

    return {"items": items, "correct_order": correct_order}


# --- Option shuffling --------------------------------------------------------
# The generated bank has a strong position/length bias (correct answers land
# on "B" ~71% of the time, and the longest option is correct ~62% of the
# time) — an artifact of how it was LLM-generated. Re-lettering options at
# presentation time neutralizes the position bias without touching the
# 1,389 source files. Sequence questions are left alone: their lettered
# options are never shown to the user (they get the reorder UI instead).

def random_letter_map(q: dict, rng=None):
    """A random old-letter -> new-letter permutation for q's options, or
    None if q shouldn't be relettered (sequence questions)."""
    if parse_sequence(q):
        return None
    letters = sorted(q["options"])
    shuffled = letters[:]
    (rng or random).shuffle(shuffled)
    return dict(zip(letters, shuffled))


def remap_options(q: dict, mapping):
    """Return a copy of q with options/answer relettered per mapping
    (old_letter -> new_letter). No-op if mapping is falsy.

    Rebuilding the dict via a comprehension preserves the ORIGINAL
    iteration order (just with new key labels) — since dicts (and Jinja's
    `.items()` loop over them) iterate in insertion order, that would relabel
    the correct answer but leave it sitting in the same visual row every
    time. Sorting by the new letter afterward randomizes the display
    position along with the label, since the new letters are themselves a
    random permutation.
    """
    if not mapping:
        return q
    new_options = {mapping[old]: text for old, text in q["options"].items()}
    new_options = dict(sorted(new_options.items()))
    new_answer = sorted(mapping[a] for a in q["answer"])
    return {**q, "options": new_options, "answer": new_answer}


# --- Scoring (with partial credit) ------------------------------------------

def score_answer(q: dict, given):
    """Score a submitted answer against q.

    given is a list of option letters for MC/Multiple Response questions
    (order doesn't matter), or a list of item numbers in submitted order for
    sequence questions (order matters). Returns (fraction 0..1, status),
    where status is "correct" / "partial" / "incorrect".

    Partial credit for Multiple Response: (correct picks - incorrect picks)
    / total correct, floored at 0 — the standard scheme most certification
    exams use. Partial credit for sequences: fraction of positions matching
    the correct order.
    """
    seq = parse_sequence(q)
    if seq is not None:
        correct_order = seq["correct_order"]
        if len(given) != len(correct_order):
            fraction = 0.0
        else:
            matches = sum(1 for g, c in zip(given, correct_order) if g == c)
            fraction = matches / len(correct_order)
    else:
        given_set = set(given)
        answer_set = set(q["answer"])
        correct_picks = len(given_set & answer_set)
        incorrect_picks = len(given_set - answer_set)
        fraction = max(0, correct_picks - incorrect_picks) / len(answer_set)

    if fraction >= 0.999:
        status = "correct"
    elif fraction > 0:
        status = "partial"
    else:
        status = "incorrect"
    return fraction, status

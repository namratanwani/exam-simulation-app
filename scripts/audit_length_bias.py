#!/usr/bin/env python3
"""Report length-bias metrics for single-answer MC questions.

Usage:
  python3 scripts/audit_length_bias.py                  # whole bank
  python3 scripts/audit_length_bias.py modules/01-*/*/questions.md   # specific files

For each file/scope, reports: how many single-answer MC questions, average
correct-option length vs average distractor length, and what % of the time
the longest option happens to be the correct one (should be close to
1/avg_option_count if unbiased, i.e. ~25% for 4-option questions).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from question_bank import parse_sequence, parse_questions_file, load_bank, prettify


def report(questions, label):
    single = [q for q in questions if len(q["answer"]) == 1 and not parse_sequence(q)]
    if not single:
        print(f"{label}: no single-answer MC questions")
        return
    correct_lens = [len(q["options"][q["answer"][0]]) for q in single]
    wrong_lens = [len(t) for q in single for letter, t in q["options"].items() if letter != q["answer"][0]]
    longest_is_correct = sum(
        1 for q in single
        if max(q["options"], key=lambda letter: len(q["options"][letter])) == q["answer"][0]
    )
    avg_correct = sum(correct_lens) / len(correct_lens)
    avg_wrong = sum(wrong_lens) / len(wrong_lens)
    pct_longest = 100 * longest_is_correct / len(single)
    print(f"{label}")
    print(f"  {len(single)} single-answer questions | "
          f"avg correct={avg_correct:.0f} chars | avg distractor={avg_wrong:.0f} chars | "
          f"ratio={avg_correct / avg_wrong:.2f}x | longest-is-correct={pct_longest:.0f}%")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for path_str in sys.argv[1:]:
            path = Path(path_str).resolve()
            path_name = prettify(path.parent.parent.name)
            module_name = prettify(path.parent.name)
            questions = parse_questions_file(path, path_name, module_name)
            report(questions, f"{path_name} / {module_name}")
    else:
        report(load_bank(), "FULL BANK")

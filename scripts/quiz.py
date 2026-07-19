#!/usr/bin/env python3
"""AI-103 exam simulator — CLI quiz over the collected question bank.

Reads modules/*/*/questions.md, lets you pick section-wise, module-wise,
or full-exam quizzes with a random sample of N questions, then shows your
score and a review of anything you got wrong.
"""

import random
import re
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from question_bank import (  # noqa: E402
    load_bank, parse_sequence, random_letter_map, remap_options, score_answer, MODULES_DIR,
)

WIDTH = 88


def wrap(text, indent=""):
    return textwrap.fill(text, width=WIDTH, initial_indent=indent, subsequent_indent=indent)


def prompt_choice(label, options):
    print(f"\n{label}")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        raw = input("> ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1]
        print(f"Enter a number between 1 and {len(options)}.")


def prompt_int(label, minimum, maximum, default):
    print(f"\n{label} (default {default}, {minimum}-{maximum})")
    while True:
        raw = input("> ").strip()
        if raw == "":
            return default
        if raw.isdigit() and minimum <= int(raw) <= maximum:
            return int(raw)
        print(f"Enter a number between {minimum} and {maximum}, or leave blank for {default}.")


def choose_pool(bank):
    print("\nQuiz type:")
    print("  1. Section-wise")
    print("  2. Module-wise")
    print("  3. Full exam (all modules)")
    print("  0. Quit")
    mode = input("> ").strip()

    if mode == "0":
        return None, None
    if mode not in ("1", "2", "3"):
        print("Invalid choice.")
        return choose_pool(bank)

    if mode == "3":
        return bank, "Full exam"

    paths = sorted({q["path"] for q in bank})
    path = prompt_choice("Learning path:", paths)
    modules = sorted({q["module"] for q in bank if q["path"] == path})
    module = prompt_choice("Module:", modules)

    if mode == "2":
        pool = [q for q in bank if q["path"] == path and q["module"] == module]
        return pool, f"{path} / {module}"

    sections = list(dict.fromkeys(
        q["section"] for q in bank if q["path"] == path and q["module"] == module
    ))
    section = prompt_choice("Section:", sections)
    pool = [
        q for q in bank
        if q["path"] == path and q["module"] == module and q["section"] == section
    ]
    return pool, f"{path} / {module} / {section}"


def ask_question(i, total, q):
    print("\n" + "=" * WIDTH)
    print(f"Question {i}/{total}  [{q['path']} / {q['module']} / {q['section']}]")
    print("-" * WIDTH)
    print(wrap(q["stem"]))

    seq = parse_sequence(q)
    if seq:
        print("\nSteps (in arbitrary order):")
        for n, text in seq["items"]:
            print(f"  {n}. {text}")
        valid = {n for n, _ in seq["items"]}
        example = ",".join(str(n) for n, _ in seq["items"])
        while True:
            raw = input(f"\nEnter the correct order as comma-separated numbers (e.g. {example}): ").strip()
            tokens = [c for c in re.split(r"[,\s]+", raw) if c]
            if all(t.lstrip("-").isdigit() for t in tokens):
                nums = [int(t) for t in tokens]
                if sorted(nums) == sorted(valid) and len(nums) == len(valid):
                    return nums
            print(f"Enter each of {sorted(valid)} exactly once, separated by commas.")

    print()
    for letter in sorted(q["options"]):
        print(f"  {letter}. {q['options'][letter]}")

    multi = len(q["answer"]) > 1
    hint = f" (choose {len(q['answer'])}, e.g. A,C)" if multi else " (e.g. B)"
    while True:
        raw = input(f"\nYour answer{hint}: ").strip().upper()
        letters = [c for c in re.split(r"[,\s]+", raw) if c]
        if letters and all(c in q["options"] for c in letters):
            return sorted(set(letters))
        print("Enter valid option letter(s) matching the choices shown.")


def run_quiz(pool, label):
    if not pool:
        print("No questions found for that selection.")
        return

    max_n = len(pool)
    n = prompt_int(f"How many questions? ({max_n} available in '{label}')", 1, max_n, min(10, max_n))
    sample = random.sample(pool, n)

    results = []
    for i, q in enumerate(sample, 1):
        q = remap_options(q, random_letter_map(q))
        given = ask_question(i, n, q)
        fraction, status = score_answer(q, given)
        results.append((q, given, fraction, status))

        if status == "correct":
            print("Correct!")
        elif status == "partial":
            print(f"Partially correct ({fraction * 100:.0f}%).")
        else:
            print("Incorrect.")

        seq = parse_sequence(q)
        if seq:
            print("Correct order: " + ", ".join(str(x) for x in seq["correct_order"]))
        else:
            print(f"Correct answer: {', '.join(sorted(q['answer']))}")
        if q["explanation"]:
            print(wrap(q["explanation"], indent="   "))

    score = sum(f for _, _, f, _ in results)
    pct = 100 * score / n
    print("\n" + "=" * WIDTH)
    print(f"SCORE: {score:.1f}/{n} ({pct:.0f}%)")
    print("=" * WIDTH)

    wrong = [(q, g, f) for q, g, f, s in results if s != "correct"]
    if wrong:
        print(f"\nReview — {len(wrong)} question(s) not fully correct:\n")
        for q, given, fraction in wrong:
            print("-" * WIDTH)
            print(f"[{q['path']} / {q['module']} / {q['section']}]")
            print(wrap(q["stem"]))
            seq = parse_sequence(q)
            if seq:
                print("Your order:    " + ", ".join(str(x) for x in given))
                print("Correct order: " + ", ".join(str(x) for x in seq["correct_order"]))
            else:
                for letter in sorted(q["options"]):
                    print(f"  {letter}. {q['options'][letter]}")
                print(f"Your answer: {', '.join(given)}   Correct: {', '.join(sorted(q['answer']))}")
            print(f"Score: {fraction * 100:.0f}%")
            if q["explanation"]:
                print(wrap(q["explanation"], indent="  "))
    else:
        print("\nPerfect score!")


def main():
    print("AI-103 Exam Simulator")
    print("Loading question bank...")
    bank = load_bank()
    if not bank:
        print(f"No questions found under {MODULES_DIR}. Nothing to quiz on.")
        sys.exit(1)
    print(f"Loaded {len(bank)} questions across "
          f"{len({q['path'] for q in bank})} paths / "
          f"{len({(q['path'], q['module']) for q in bank})} modules.")

    while True:
        pool, label = choose_pool(bank)
        if pool is None:
            print("Bye.")
            break
        run_quiz(pool, label)
        again = input("\nTake another quiz? (y/n): ").strip().lower()
        if again != "y":
            print("Bye.")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBye.")

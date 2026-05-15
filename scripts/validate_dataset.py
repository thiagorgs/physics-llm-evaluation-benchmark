from pathlib import Path

REQUIRED_SECTIONS = [
    "## Topic",
    "## Difficulty",
    "## Problem Statement",
    "## Expected Reasoning Skills",
    "## Target Result",
]

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS_DIR = ROOT / "problems"


def validate_problem_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    missing = [section for section in REQUIRED_SECTIONS if section not in text]
    return missing


def main() -> None:
    if not PROBLEMS_DIR.exists():
        raise FileNotFoundError(f"Problems directory not found: {PROBLEMS_DIR}")

    problem_files = sorted(PROBLEMS_DIR.rglob("*.md"))

    if not problem_files:
        print("No problem files found.")
        return

    all_valid = True

    for path in problem_files:
        missing = validate_problem_file(path)
        rel_path = path.relative_to(ROOT)

        if missing:
            all_valid = False
            print(f"[FAIL] {rel_path}")
            for section in missing:
                print(f"  Missing section: {section}")
        else:
            print(f"[OK] {rel_path}")

    if all_valid:
        print("\nAll problem files passed validation.")
    else:
        print("\nSome problem files are missing required sections.")


if __name__ == "__main__":
    main()

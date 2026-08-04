from pathlib import Path

# Folder containing this script
ROOT = Path(__file__).parent

rows = []

# Find all folders whose names are numbers (001, 002, ...)
problem_dirs = sorted(
    [d for d in ROOT.iterdir() if d.is_dir() and d.name.isdigit()],
    key=lambda x: int(x.name)
)

for folder in problem_dirs:
    number = folder.name

    # Find the solution file
    if (folder / "solution.py").exists():
        solution = f"[solution.py]({number}/solution.py)"
    elif (folder / "solution.pdf").exists():
        solution = f"[solution.pdf]({number}/solution.pdf)"
    else:
        solution = "—"

    rows.append(
        f"| {number} | {solution} | ✅ |"
    )

readme = f"""# Project Euler

My solutions to [Project Euler](https://projecteuler.net/).

## Progress

Solved **{len(problem_dirs)}** problems.

| Problem | Solution | Status |
|:-------:|:--------:|:------:|
{chr(10).join(rows)}
"""

(ROOT / "README.md").write_text(readme, encoding="utf-8")

print("README updated successfully!")
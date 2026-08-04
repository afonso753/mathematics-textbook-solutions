from pathlib import Path

# Folder containing this script
ROOT = Path(__file__).parent

rows = []
solved = 0

# Find all folders whose names are numbers (001, 002, ...)
problem_dirs = sorted(
    [d for d in ROOT.iterdir() if d.is_dir() and d.name.isdigit()],
    key=lambda x: int(x.name)
)

for folder in problem_dirs:
    number = folder.name

    solution = None

    # Check for a solution file
    if (folder / "solution.py").exists():
        solution = f"[solution.py]({number}/solution.py)"
    elif (folder / "solution.pdf").exists():
        solution = f"[solution.pdf]({number}/solution.pdf)"
    else:
        notebook = next(folder.glob("*.ipynb"), None)
        if notebook is not None:
            solution = f"[{notebook.name}]({number}/{notebook.name})"

    # Skip folders without any solution files
    if solution is None:
        continue

    solved += 1
    rows.append(f"| {number} | {solution} | ✅ |")

readme = f"""# Project Euler

My solutions to [Project Euler](https://projecteuler.net/).

## Progress

Solved **{solved}** problems.

| Problem | Solution | Status |
|:-------:|:--------:|:------:|
{chr(10).join(rows)}
"""

(ROOT / "README.md").write_text(readme, encoding="utf-8")

print("README updated successfully!")
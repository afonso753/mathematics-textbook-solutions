from pathlib import Path

# Folder containing this script
ROOT = Path(__file__).parent

# Number of problems to display in the table
DISPLAY_PROBLEMS = 100

# Total number of Project Euler problems
TOTAL_PROBLEMS = 1007

rows = []
solved = 0

# Find all folders whose names are numbers (001, 002, ...)
problem_dirs = sorted(
    [d for d in ROOT.iterdir() if d.is_dir() and d.name.isdigit()],
    key=lambda x: int(x.name)
)

folders = {int(folder.name): folder for folder in problem_dirs}


# --------------------------------------------------
# Count all solved problems
# --------------------------------------------------

for folder in problem_dirs:

    solution_exists = (
        (folder / "solution.py").exists()
        or (folder / "solution.pdf").exists()
        or next(folder.glob("*.ipynb"), None) is not None
    )

    if solution_exists:
        solved += 1


# --------------------------------------------------
# Create table for first 100 problems
# --------------------------------------------------

for i in range(1, DISPLAY_PROBLEMS + 1):

    number = f"{i:03d}"
    folder = folders.get(i)

    solution = None

    if folder is not None:

        if (folder / "solution.py").exists():
            solution = f"[solution.py]({number}/solution.py)"

        elif (folder / "solution.pdf").exists():
            solution = f"[solution.pdf]({number}/solution.pdf)"

        else:
            notebook = next(folder.glob("*.ipynb"), None)

            if notebook is not None:
                solution = f"[{notebook.name}]({number}/{notebook.name})"

    if solution is not None:
        rows.append(f"| {number} | {solution} | ✅ |")
    else:
        rows.append(f"| {number} | — | ❌ |")


# --------------------------------------------------
# Progress bar
# --------------------------------------------------

percentage = solved / TOTAL_PROBLEMS * 100

bar_length = 30
filled = round(bar_length * solved / TOTAL_PROBLEMS)

progress_bar = (
    "█" * filled +
    "░" * (bar_length - filled)
)


# --------------------------------------------------
# Create README
# --------------------------------------------------

readme = f"""# Project Euler

My solutions to [Project Euler](https://projecteuler.net/).

## Progress

**{solved} / {TOTAL_PROBLEMS} problems solved — {percentage:.1f}%**

`{progress_bar}`

## Problems 1–100

| Problem | Solution | Status |
| :-----: | :------: | :----: |
{chr(10).join(rows)}
"""

(ROOT / "README.md").write_text(readme, encoding="utf-8")

print("README updated successfully!")
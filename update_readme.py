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

# Create a dictionary so we can easily find existing problem folders
folders = {int(folder.name): folder for folder in problem_dirs}

# Show problems 1 to 100
for i in range(1, 101):

    # Format problem number as 3 digits
    number = f"{i:03d}"

    # Check whether the problem folder exists
    folder = folders.get(i)

    solution = None

    if folder is not None:

        # Check for a solution file
        if (folder / "solution.py").exists():
            solution = f"[solution.py]({number}/solution.py)"

        elif (folder / "solution.pdf").exists():
            solution = f"[solution.pdf]({number}/solution.pdf)"

        else:
            notebook = next(folder.glob("*.ipynb"), None)

            if notebook is not None:
                solution = f"[{notebook.name}]({number}/{notebook.name})"

    # Problem solved
    if solution is not None:
        solved += 1
        rows.append(f"| {number} | {solution} | ✅ |")

    # Problem not solved
    else:
        rows.append(f"| {number} | — | ❌ |")


readme = f"""# Project Euler

My solutions to [Project Euler](https://projecteuler.net/).

## Progress

Solved **{solved}/100** problems.

| Problem | Solution | Status |
| :-----: | :------: | :----: |
{chr(10).join(rows)}
"""

(ROOT / "README.md").write_text(readme, encoding="utf-8")

print("README updated successfully!")
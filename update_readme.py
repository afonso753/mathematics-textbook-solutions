from pathlib import Path

# ============================================================
# Configuration
# ============================================================

ROOT = Path(__file__).parent

# Number of problems displayed in the README table
DISPLAY_PROBLEMS = 100

# Total number of Project Euler problems
TOTAL_PROBLEMS = 1007


# ============================================================
# Find problem folders
# ============================================================

problem_dirs = sorted(
    [
        d for d in ROOT.iterdir()
        if d.is_dir() and d.name.isdigit()
    ],
    key=lambda x: int(x.name)
)

# Dictionary for quick access:
# {1: Path(.../001), 2: Path(.../002), ...}
folders = {
    int(folder.name): folder
    for folder in problem_dirs
}


# ============================================================
# Determine whether a problem has been solved
# ============================================================

def get_solution(folder):
    """Return the Markdown link to a solution, or None."""

    if folder is None:
        return None

    # Python solution
    if (folder / "solution.py").exists():
        return "[solution.py]({}/solution.py)".format(folder.name)

    # PDF solution
    if (folder / "solution.pdf").exists():
        return "[solution.pdf]({}/solution.pdf)".format(folder.name)

    # Jupyter notebook
    notebook = next(folder.glob("*.ipynb"), None)

    if notebook is not None:
        return f"[{notebook.name}]({folder.name}/{notebook.name})"

    return None


# ============================================================
# Count ALL solved problems
# ============================================================

solved = 0

for folder in problem_dirs:

    solution = get_solution(folder)

    if solution is not None:
        solved += 1


# ============================================================
# Calculate progress
# ============================================================

percentage = solved / TOTAL_PROBLEMS * 100


# ============================================================
# Generate SVG progress bar
# ============================================================

svg_width = 500
svg_height = 24

# Percentage of the bar that should be filled
fill_width = svg_width * solved / TOTAL_PROBLEMS

# Don't let a tiny value become visually invisible
if solved > 0:
    fill_width = max(fill_width, 2)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
    width="{svg_width}"
    height="{svg_height}"
    viewBox="0 0 {svg_width} {svg_height}">

    <rect
        x="0"
        y="0"
        width="{svg_width}"
        height="{svg_height}"
        rx="12"
        fill="#e1e4e8"/>

    <rect
        x="0"
        y="0"
        width="{fill_width:.2f}"
        height="{svg_height}"
        rx="12"
        fill="#2ea043"/>

</svg>
"""

(ROOT / "progress.svg").write_text(
    svg,
    encoding="utf-8"
)


# ============================================================
# Create table for Problems 1–100
# ============================================================

rows = []

for i in range(1, DISPLAY_PROBLEMS + 1):

    # Format as 001, 002, ..., 100
    number = f"{i:03d}"

    folder = folders.get(i)

    solution = get_solution(folder)

    if solution is not None:
        rows.append(
            f"| {number} | {solution} | ✅ |"
        )
    else:
        rows.append(
            f"| {number} | — | ❌ |"
        )


# ============================================================
# Generate README
# ============================================================

readme = f"""# Project Euler

My solutions to [Project Euler](https://projecteuler.net/).

## Progress

**{solved} / {TOTAL_PROBLEMS} problems solved — {percentage:.1f}%**

<img src="progress.svg" width="500">

## Problems 1–100

| Problem | Solution | Status |
| :-----: | :------: | :----: |
{chr(10).join(rows)}
"""


# ============================================================
# Write README
# ============================================================

(ROOT / "README.md").write_text(
    readme,
    encoding="utf-8"
)

print("README updated successfully!")
print(f"Solved: {solved}/{TOTAL_PROBLEMS} ({percentage:.1f}%)")
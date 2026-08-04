from pathlib import Path

ROOT = Path(__file__).parent

rows = []

problem_dirs = sorted(
    [d for d in ROOT.iterdir() if d.is_dir() and d.name.isdigit()],
    key=lambda x: int(x.name)
)

for folder in problem_dirs:
    number = folder.name

    py = "✅" if (folder / "solution.py").exists() else "—"
    pdf = "✅" if (folder / "solution.pdf").exists() else "—"
    nb = next(folder.glob("*.ipynb"), None)

    py_link = (
        f"[solution.py]({number}/solution.py)"
        if py == "✅"
        else "—"
    )

    pdf_link = (
        f"[solution.pdf]({number}/solution.pdf)"
        if pdf == "✅"
        else "—"
    )

    nb_link = (
        f"[notebook]({number}/{nb.name})"
        if nb is not None
        else "—"
    )

    rows.append(
        f"| {number} | {py_link} | {pdf_link} | {nb_link} |"
    )

readme = f"""# Project Euler Solutions

My solutions to Project Euler.

## Progress

Solved **{len(problem_dirs)}** problems.

| Problem | Python | PDF | Notebook |
|---------:|:------:|:---:|:--------:|
{chr(10).join(rows)}
"""

(ROOT / "README.md").write_text(readme, encoding="utf-8")

print("README updated.")

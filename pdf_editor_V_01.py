from pypdf import PdfMerger

merger = PdfMerger()

from pathlib import Path

reports_dir = (
    Path.home()
    / "OneDrive"
    / "Desktop"
    / "Programmieren"
    / "PDF-Merger"
)

for path in reports_dir.glob("*pdf"):
    print(path.name)

for path in reports_dir.glob("*pdf"):
    merger.append(path)
    merger.write("result.pdf")
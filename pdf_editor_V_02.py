from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["test1.pdf", "test2.pdf"]:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
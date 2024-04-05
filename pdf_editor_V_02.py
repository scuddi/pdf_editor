import os
import io
from PyPDF2 import PdfReader, PdfMerger

def find_pdfs(directory):
    found_pdf_files = []

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            found_pdf_files.append(os.path.join(directory, filename))

    print(found_pdf_files)
    return found_pdf_files

def merge_pdfs(pdf_file_list, target_directory, master_file_name):


    pdf_merger = PdfMerger()

    for pdf_file in pdf_file_list:
        with open(pdf_file, "rb") as f:
            pdf_reader = PdfReader(f)
            pdf_merger.append(pdf_reader)

    save_location = os.path.join(target_directory, master_file_name)
    with open(save_location, "wb") as f:
        pdf_merger.write(f)

directory = input("Wie lautet der gewünschte Dateipfad? ")
find_pdfs(directory)

pdf1_path = input("Erstes PDF File: ")
pdf2_path = input("Zweites PDF File: ")
pdf_file_list = [pdf1_path, pdf2_path]
target_directory = input("Wo soll das PDF gespeichert werdern? ")
master_file_name = input("Wie soll das zusammengefügte PDF heißen? ")
merge_pdfs(pdf_file_list, target_directory, master_file_name)
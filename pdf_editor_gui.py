import customtkinter
import os
import io
from PyPDF2 import PdfReader, PdfMerger

# functions and variables for the merger

found_pdf_files = []
pdf1_path = []
pdf2_path = []
pdf_file_list = []
target_directory = ""
master_file_name = ""

def find_pdfs():

    directory = check_files_file_path.get()
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            found_pdf_files.append(os.path.join(directory, filename))

    show_files_in_file_path.configure(text = found_pdf_files)
    return found_pdf_files

def merge_pdfs():


    pdf_merger = PdfMerger()

    pdf1_path = first_pdf_file_path_entry.get()
    pdf2_path = second_pdf_file_path_entry.get()

    pdf_file_list = [pdf1_path, pdf2_path]
    target_directory = saving_file_path_entry.get()
    master_file_name = name_of_merged_pdf_entry.get()


    for pdf_file in pdf_file_list:
        with open(pdf_file, "rb") as f:
            pdf_reader = PdfReader(f)
            pdf_merger.append(pdf_reader)

    save_location = os.path.join(target_directory, master_file_name)
    with open(save_location, "wb") as f:
        pdf_merger.write(f)

# GUI
# general appearance of window

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()

app.geometry("600x520")
app.title("PDF Editor by KS")

# main function for buttons to load content into main_frame

tab_values = ["Startseite", "PDF-Merger", "PDF-Snipping", "PDF-Converter"]

# main function for buttons to load content into main_frame

def tab_click(button_value):
    if button_value == "Startseite":
        starting_frame_set()
    elif button_value == "PDF-Merger":
        pdf_merger_frame()
    elif button_value == "PDF-Snipping":
        pdf_snipping_frame()
    elif button_value == "PDF-Converter":
        pdf_converter_frame()

def starting_frame_set():
    starting_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = "ew")
    merger_frame.grid_forget()
    snipping_frame.grid_forget()
    converter_frame.grid_forget()

def pdf_merger_frame():
    merger_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = "ew")
    starting_frame.grid_forget()
    snipping_frame.grid_forget()
    converter_frame.grid_forget()

def pdf_snipping_frame():
    snipping_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = "ew")
    starting_frame.grid_forget()
    merger_frame.grid_forget()
    converter_frame.grid_forget()

def pdf_converter_frame():
    converter_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = "ew")
    starting_frame.grid_forget()
    merger_frame.grid_forget()
    snipping_frame.grid_forget()

# navigation bar / tab bar

tabs_button = customtkinter.CTkSegmentedButton(master = app,
                                               values = tab_values,
                                               width = 580,
                                               command = tab_click
                                               )
tabs_button.set("Startseite")

# Startseite - Hinweis

starting_frame = customtkinter.CTkFrame(master = app, width = 580, height = 440)

hinweis = customtkinter.CTkLabel(master = starting_frame,
                                 width = 560,
                                 height = 430,
                                 text = "Wilkommen in meinem PDF-Editor\n\n"
                                        "Hier entstehen verschiedene Funktionen eines PDF-Editors.\n\n"
                                        "Die verschiedenen Funktionen sind/werden sein: \n\n"
                                        "    - PDF-Merger zum zusammenführen von zwei PDFs\n"
                                        "    - PDF-Snipping zum entfernen einzelner Seiten\n"
                                        "    - PDF-Converter zum transformieren von Word zu PDFs und anders herum")

# merger tab

merger_frame = customtkinter.CTkFrame(master = app, width = 580, height = 430)

merger_message = customtkinter.CTkLabel(master = merger_frame,
                                        width = 560,
                                        height = 10,
                                        text = "Hier können PDFs zusammengefügt werden."
                                        )

check_files_messages = customtkinter.CTkLabel(master = merger_frame,
                                              width = 250,
                                              height = 5,
                                              text = "In welchem Dateipfad befinden sich PDFs zum mergen? :")

check_files_file_path = customtkinter.CTkEntry(master = merger_frame,
                                               width = 560,
                                               height = 10,
                                               placeholder_text = "Dateipfad, in dem vorhandene PDFS angezeigt werden sollen.")

check_files_button = customtkinter.CTkButton(master = merger_frame,
                                             text = "PDFs anzeigen",
                                             command = find_pdfs
                                             )

show_files_in_file_path = customtkinter.CTkLabel(master = merger_frame,
                                                 width = 560,
                                                 height = 30,
                                                 text = found_pdf_files,
                                                 fg_color = "grey",
                                                 corner_radius = 10,
                                                 text_color = "black")

first_pdf_file_path = customtkinter.CTkLabel(master = merger_frame,
                                             width = 250,
                                             height = 5,
                                             text = "Dateipfad des ersten PDFs:                                           ")

# warum auch immer wird hier first_pdf_file_path nicht linksbündig eingesetzt, außer der Text ist länger. Deswegen die vielen Leerzeichen

first_pdf_file_path_entry = customtkinter.CTkEntry(master = merger_frame,
                                                   width = 560,
                                                   height = 10,
                                                   placeholder_text = "Dateipfad des ersten PDFs hier eingeben")

second_pdf_file_path = customtkinter.CTkLabel(master = merger_frame,
                                              width = 250,
                                              height = 5,
                                              text = "Dateipfad des zweiten PDFs:                                           ")

second_pdf_file_path_entry = customtkinter.CTkEntry(master = merger_frame,
                                                    width = 560,
                                                    height = 10,
                                                    placeholder_text = "Dateipfad des zweiten PDFs hier eingeben")

saving_file_path = customtkinter.CTkLabel(master = merger_frame,
                                          width = 250,
                                          height = 5,
                                          text = "Wo soll das zusammengefügte PDF gespeichert werden? :"
                                          )

saving_file_path_entry = customtkinter.CTkEntry(master = merger_frame,
                                                width = 560,
                                                height = 10,
                                                placeholder_text = "Hier den gewünschten Speicherort (als Dateipfad) eintragen")

name_of_merged_pdf = customtkinter.CTkLabel(master = merger_frame,
                                            width = 250,
                                            height = 5,
                                            text = "Wie soll das zusammengefügte neue PDF heißen? ")

name_of_merged_pdf_entry = customtkinter.CTkEntry(master = merger_frame,
                                                  width = 560,
                                                  height = 5,
                                                  placeholder_text = "Hier den gewünschten Namen eingeben")

merge_button = customtkinter.CTkButton(master = merger_frame,
                                       text = "Merge",
                                       width = 200,
                                       command = merge_pdfs
                                       )

# snipping frame

snipping_frame = customtkinter.CTkFrame(master = app, width = 580, height = 430)

snipping_message = customtkinter.CTkLabel(master = snipping_frame,
                                          width = 560,
                                          height = 200,
                                          text = "Hier können einzelne Seiten aus PDFs entfernt werden."
                                          )

# converter frame

converter_frame = customtkinter.CTkFrame(master = app, width = 580, height = 430)

converter_message = customtkinter.CTkLabel(master = converter_frame,
                                           width = 560,
                                           height = 200,
                                           text = "Hier können Sie (Word-) Dateien in PDFs umwandeln."
                                           )

# define grid

app.columnconfigure((0,1), weight = 0)
app.rowconfigure((0,1), weight = 0)

# grid for gui layout

tabs_button.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady= 10, sticky = "new")
starting_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = "ew")
hinweis.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 15, sticky = "nsew")

# grid in merger frame / merger tab

merger_message.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 15, sticky = "nsew")
check_files_messages.grid(row = 2, column = 0, columnspan = 1, padx = 10, pady = 8, sticky = "nw")
check_files_button.grid(row = 2, column = 1, columnspan = 1, padx = 25, pady = 2, sticky = "nw")
check_files_file_path.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 5, sticky = "nw")
show_files_in_file_path.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 8, sticky = "nw")
first_pdf_file_path.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 5, sticky = "nw")
first_pdf_file_path_entry.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 5, sticky = "nw")
second_pdf_file_path.grid(row = 7, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = "nw")
second_pdf_file_path_entry.grid(row = 8, column = 0, columnspan = 2, padx = 10, pady = 5, sticky = "nw")
saving_file_path.grid(row = 9, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = "nw")
saving_file_path_entry.grid(row = 10, column = 0, columnspan = 2, padx = 10, pady = 5, sticky = "nw")
name_of_merged_pdf.grid(row = 11, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = "nw")
name_of_merged_pdf_entry.grid(row = 12, column = 0, columnspan = 2, padx = 10, pady = 5, sticky = "nw")
merge_button.grid(row = 13, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = "nsew")

snipping_message.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 15, sticky = "nsew")
converter_message.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 15, sticky = "nsew")

app.mainloop()
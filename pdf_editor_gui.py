import customtkinter

# general appearance of window

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()

app.geometry("600x500")
app.title("PDF Editor by KS")

# main function for buttons to load content into main_frame

tab_values = ["Startseite", "PDF-Merger", "PDF-Snipping", "PDF-Converter"]

# main function for buttons to load content into main_frame

current_frame = None
starting_frame = None
merger_frame = None

def tab_click(button_value):
    print(button_value)
    if button_value == "Startseite":
        current_frame = starting_frame_set()
    elif button_value == "PDF-Merger":
        current_frame = pdf_merger_frame()

def starting_frame_set():
    starting_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = "ew")

def pdf_merger_frame():
    merger_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = "ew")


# navigation bar / tab bar

tabs_button = customtkinter.CTkSegmentedButton(master = app,
                                               values = tab_values,
                                               width = 580,
                                               command = tab_click
                                               )
tabs_button.set("Startseite")

# Startseite - Hinweis

starting_frame = customtkinter.CTkFrame(master = app, width = 580, height = 430)

hinweis = customtkinter.CTkLabel(master = starting_frame,
                                 width = 560,
                                 height = 410,
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
                                        height = 200,
                                        text = "Hier können PDFs zusammengefügt werden."
                                        )

# define grid

app.columnconfigure((0,1), weight = 0)
app.rowconfigure((0,1), weight = 0)

# grid for gui layout

tabs_button.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady= 10, sticky = "new")
starting_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = "ew")
hinweis.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 15, sticky = "nsew")
#merger_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = "ew")
merger_message.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 15, sticky = "nsew")

app.mainloop()
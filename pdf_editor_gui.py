import customtkinter

# general appearance of window

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()

app.geometry("600x500")
app.title("PDF Editor by KS")

# main function for buttons to load content into main_frame

"""def main_function(value):"""

# navigation bar / tab bar

tabs_button = customtkinter.CTkSegmentedButton(master = app, values = ["Startseite", "PDF-Merger", "PDF-Snipping", "PDF-Converter"],
                                               width = 580,
                                               #command = main_function)
tabs_button.set("Startseite")


main_frame = customtkinter.CTkFrame(master=app, width = 580, height = 430)

# Startseite - Hinweis


hinweis = customtkinter.CTkLabel(master = main_frame,
                                 width = 560,
                                 height = 410,
                                 text = "Wilkommen in meinem PDF-Editor\n\n"
                                        "Hier entstehen verschiedene Funktionen eines PDF-Editors.\n\n"
                                        "Die verschiedenen Funktionen sind/werden sein: \n\n"
                                        "    - PDF-Merger zum zusammenführen von zwei PDFs\n"
                                        "    - PDF-Snipping zum entfernen einzelner Seiten\n"
                                        "    - PDF-Converter zum transformieren von Word zu PDFs und anders herum")


# define grid

app.columnconfigure((0,1), weight = 0)
app.rowconfigure((0,1), weight = 0)

# grid for gui layout

tabs_button.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady= 10, sticky = "new")
main_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = "ew")
hinweis.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 15, sticky = "nsew")

app.mainloop()
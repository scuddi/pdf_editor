import customtkinter

# general appearance of window

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()

app.geometry("600x500")
app.title("PDF Editor by KS")

# navigation bar / tab bar

tabs_button = customtkinter.CTkSegmentedButton(master = app, values = ["Startseite", "PDF-Merger", "PDF-Snipping", "PDF-Converter"], width = 580)
tabs_button.set("Startseite")

# Startseite - Hinweis

frame1 = customtkinter.CTkFrame(master=app, fg_color="#ad3f37", border_color="#240d0c", border_width=2, width = 580)

#hinweis = customtkinter.CTkLabel(master)


# define grid

app.columnconfigure((0,1), weight = 0)
app.rowconfigure((0,1), weight = 0)

# grid for gui layout

tabs_button.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady= 10, sticky = "new")
frame1.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = "ew")

app.mainloop()
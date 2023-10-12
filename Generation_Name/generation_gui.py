import customtkinter as ctk


ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green




app = ctk.CTk()  # create CTk window like you do with the Tk window
app.title("Generation Name")
app.geometry("600x600")
def genaration():

	b_year = int(entyear.get())
	if b_year >= 1901 and b_year <= 1924:
		distext.delete(1.0, "end")
		distext.insert(1.0, 'The Greatest Generation')
	elif b_year >=1925 and b_year <= 1945:
		distext.delete(1.0, "end")
		distext.insert(1.0, "The Silent Generation")
	elif b_year >= 1946 and b_year <= 1964:
		distext.delete(1.0, "end")
		distext.insert(1.0, "The Baby Boomers Generation")
	elif b_year >= 1965 and b_year <= 1979:
		distext.delete(1.0, "end")
		distext.insert(1.0, "You belong to Generation X")
	elif b_year >= 1980 and b_year <= 1994:
		distext.delete(1.0, "end")
		distext.insert(1.0, "You are a Millennial")
	elif b_year >= 1995 and b_year <= 2012:
		distext.delete(1.0, "end")
		distext.insert(1.0, "You belong to Gen Z")
	elif b_year >= 2013 and b_year <= 2025:
		distext.delete(1.0, "end")
		distext.insert(1.0, "You belong to Gen Alpha")
	else:
		distext.delete(1.0, "end")
		distext.insert(1.0, "Generation Name Not Known")


labeltext = ctk.CTkLabel(master=app, text="Enter Year of Birth", font=('Candara', 30))
labeltext.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

entyear = ctk.CTkEntry(master=app, height=50,width=400,font=('Candara', 30))
entyear.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(master=app, text="Generate", height=50,width=100, command=lambda :genaration())
button.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

distext = ctk.CTkTextbox (master=app, width=550, font=('Candara', 40))
distext.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

app.mainloop()
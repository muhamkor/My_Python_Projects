"""
Created on Thu Sep  7 22:28:01 2023

@author: muham
"""

import customtkinter as ctk

# Global variable to store the current calculation
calculation = ""

# Function to add a symbol to the calculation
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    # Clear the text box and insert the new calculation
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Function to evaluate the calculation
def evaluate_calculation():
    global calculation
    try:
        # Evaluate the calculation using the eval() function
        calculation = str(eval(calculation))
        # Clear the text box and insert the result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        # Clear the text box and display an error message
        clear_field()
        text_result.insert(1.0, "Error")

# Function to clear the text box
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Create the main window
root = ctk.CTk()
root.title('Calculator')

# Set the window size
root.geometry('405x325')

# Create a text box to display the calculation and result
text_result = ctk.CTkTextbox(master=root, height=4, width=400, font=('Candara', 40))
text_result.grid(columnspan=5)

# Create buttons for the numbers 0-9
btn_1 = ctk.CTkButton(master=root, text="1", command=lambda: add_to_calculation(1), width=90, font=('Candara', 40))
btn_1.grid(row=2, column=1)
btn_2 = ctk.CTkButton(master=root, text="2", command=lambda: add_to_calculation(2), width=90, font=('Candara', 40))
btn_2.grid(row=2, column=2)
btn_3 = ctk.CTkButton(master=root, text="3", command=lambda: add_to_calculation(3), width=90, font=('Candara', 40))
btn_3.grid(row=2, column=3)
btn_4 = ctk.CTkButton(master=root, text="4", command=lambda: add_to_calculation(4), width=90, font=('Candara', 40))
btn_4.grid(row=3, column=1)
btn_5 = ctk.CTkButton(master=root, text="5", command=lambda: add_to_calculation(5), width=90, font=('Candara', 40))
btn_5.grid(row=3, column=2)
btn_6 = ctk.CTkButton(master=root, text="6", command=lambda: add_to_calculation(6), width=90, font=('Candara', 40))
btn_6.grid(row=3, column=3)
btn_7 = ctk.CTkButton(master=root, text="7", command=lambda: add_to_calculation(7), width=90, font=('Candara', 40))
btn_7.grid(row=4, column=1)
btn_8 = ctk.CTkButton(master=root, text="8", command=lambda: add_to_calculation(8), width=90, font=('Candara', 40))
btn_8.grid(row=4, column=2)
btn_9 = ctk.CTkButton(master=root, text="9", command=lambda: add_to_calculation(9), width=90, font=('Candara', 40))
btn_9.grid(row=4, column=3)
btn_0 = ctk.CTkButton(master=root, text="0", command=lambda: add_to_calculation(0), width=90, font=('Candara', 40))
btn_0.grid(row=5, column=2)

# Create buttons for the arithmetic operators
btn_plus = ctk.CTkButton(master=root, text="+", command=lambda: add_to_calculation

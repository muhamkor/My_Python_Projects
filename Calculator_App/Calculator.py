"""
Created on Thu Sep  7 22:28:01 2023

@author: muham
"""

import customtkinter as ctk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,'end')
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,'end')

root = ctk.CTk()
root.title('Calculator')

root.geometry('405x325')

text_result = ctk.CTkTextbox(master = root, height=4, width=400, font=('Candara', 40))
text_result.grid(columnspan=5)

btn_1 = ctk.CTkButton(master = root, text="1", command = lambda:add_to_calculation(1), width= 90, font=('Candara', 40))
btn_1.grid(row=2,column=1)
btn_2 = ctk.CTkButton(master = root, text="2", command = lambda:add_to_calculation(2), width= 90, font=('Candara', 40))
btn_2.grid(row=2,column=2)
btn_3 = ctk.CTkButton(master = root, text="3", command = lambda:add_to_calculation(3), width= 90, font=('Candara', 40))
btn_3.grid(row=2,column=3)
btn_4 = ctk.CTkButton(master = root, text="4", command = lambda:add_to_calculation(4), width= 90, font=('Candara', 40))
btn_4.grid(row=3,column=1)
btn_5 = ctk.CTkButton(master = root, text="5", command = lambda:add_to_calculation(5), width= 90, font=('Candara', 40))
btn_5.grid(row=3,column=2)
btn_6 = ctk.CTkButton(master = root, text="6", command = lambda:add_to_calculation(6), width= 90, font=('Candara', 40))
btn_6.grid(row=3,column=3)
btn_7 = ctk.CTkButton(master = root, text="7", command = lambda:add_to_calculation(7), width= 90, font=('Candara', 40))
btn_7.grid(row=4,column=1)
btn_8 = ctk.CTkButton(master = root, text="8", command = lambda:add_to_calculation(8), width= 90, font=('Candara', 40))
btn_8.grid(row=4,column=2)
btn_9 = ctk.CTkButton(master = root, text="9", command = lambda:add_to_calculation(9), width= 90, font=('Candara', 40))
btn_9.grid(row=4,column=3)
btn_0 = ctk.CTkButton(master = root, text="0", command = lambda:add_to_calculation(0), width= 90, font=('Candara', 40))
btn_0.grid(row=5,column=2)

btn_plus = ctk.CTkButton(master = root, text="+", command = lambda:add_to_calculation("+"), width= 90, font=('Candara', 40))
btn_plus.grid(row=2,column=4)
btn_min = ctk.CTkButton(master = root, text="-", command = lambda:add_to_calculation("-"), width= 90, font=('Candara', 40))
btn_min.grid(row=3,column=4)
btn_mul = ctk.CTkButton(master = root, text="x", command = lambda:add_to_calculation("*"), width= 90, font=('Candara', 40))
btn_mul.grid(row=4,column=4)
btn_div = ctk.CTkButton(master = root, text="/", command = lambda:add_to_calculation("/"), width= 90, font=('Candara', 40))
btn_div.grid(row=5,column=4)

btn_clear = ctk.CTkButton(master = root, text="C", command = clear_field, width= 90, font=('Candara', 40))
btn_clear.grid(row=5,column=1)
btn_equal = ctk.CTkButton(master = root, text="=", command = evaluate_calculation, width= 90, font=('Candara', 40))
btn_equal.grid(row=5,column=3)

root.mainloop()

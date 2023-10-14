"""
Created on Thu Aug 10 21:17:59 2023

@author: mkora
"""

import calendar
import customtkinter as ctk
ctk.set_appearance_mode('System')

def mycalendar(): # This is a function we created for our calendar
    try :
        yy = int(yr.get()) # creating a variable for year
        mm = int(mnt.get()) # creating a variable 
        vcal.insert(1.0,calendar.month(yy, mm,7,2))# print the coresponding month
    
    except:
        vcal.insert(1.0,'Error')
   
        
root = ctk.CTk()
root.title('Calender')
root.geometry("1150x900")

title = ctk.CTkLabel(master = root, text="Calendar",font=('arial',20))
title.pack(pady=20)

btn_cal = ctk.CTkButton(master = root,text="Click for Calendar",command = mycalendar)
btn_cal.pack(pady=20)

mnt = ctk.CTkEntry(root,font=('arial',20))
mnt.place(x=80, y=70)
mnt_placeholder = ctk.CTkLabel(master = root,text="Month:", font=('arial',20))
mnt_placeholder.place(x=10, y=70)

yr = ctk.CTkEntry(root,font=('arial',20))
yr.place(x=330, y=70)
yr_placeholder = ctk.CTkLabel(master = root,text="Year:", font=('arial',20))
yr_placeholder.place(x=250, y=70)

vcal = ctk.CTkTextbox(master = root,font=('arial', 30),width=1100,height=700)
vcal.place(x=20, y=160)

root.mainloop()
    

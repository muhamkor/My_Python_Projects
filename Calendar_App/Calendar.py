# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:17:59 2023

@author: mkora
"""

import calendar
import tkinter as tk

def mycalendar(): # This is a function we created for our calendar
    try :
        yy = int(yr.get()) # creating a variable for year
        mm = int(mnt.get()) # creating a variable 
        vcal.insert(1.0,calendar.month(yy, mm,5,3))# print the coresponding month
    
    except:
        mycalendar()
   
        
root = tk.Tk()
root.title('Calender')
root.geometry("300x400")

title = tk.Label(root, text="Calendar", fg='red')
title.pack()



btn_cal = tk.Button(root,text="Click for Calendar",command = mycalendar)
btn_cal.pack()

mnt = tk.Entry(root)
mnt.pack(pady=20)
mnt_placeholder = tk.Label(root,text="Month", font=('arial',8))
mnt_placeholder.place(x=20, y=65)

yr = tk.Entry(root)
yr.pack(pady=20)
yr_placeholder = tk.Label(root,text="Year", font=('arial',8))
yr_placeholder.place(x=20, y=125)


vcal = tk.Text(root,font=('Algerian', 14))
vcal.pack(padx=40, pady=40)





root.mainloop()
    

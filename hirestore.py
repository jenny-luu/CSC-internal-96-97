"""This program will create a save customer details and print out like a bills, this program can keep check and
manager the customer information and the items have issused in Julie Hire store"""

from tkinter import *
import tkinter as tk
from tkinter import ttk

# Quit function
def quit():
     main_window.destroy()

#print details of all customer details
def print_customer_details ():
    global j_names, total_entries, name_count
    name_count = 0
    Label(main_window, font="times 15 bold",text="Row", bg="pink").grid(column=0,row=7)
    Label(main_window, font='times 15 bold',text="Full name",bg ="pink").grid(column=1,row=7)
    Label(main_window, font='times 15 bold',text="Receipt number",bg ="pink").grid(column=2,row=7)
    Label(main_window, font='times 15 bold',text="Item hire",bg ="pink").grid(column=3,row=7)
    Label(main_window, font='times 15 bold',text="Quantity",bg ="pink").grid(column=4,row=7)

    while name_count < total_entries :
        Label(main_window, text=name_count,bg="sky blue").grid(column=0,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][0]),bg="pink").grid(column=1,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][1]),bg="pink").grid(column=2,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][2]),bg="pink").grid(column=3,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][3]),bg="pink").grid(column=4,row=name_count+8)
        name_count +=  1

#add the customer information to the list
def append_name ():
    global customer_details, entry_name,entry_receipt,entry_item,entry_quantity, total_entries
    if len(entry_name.get()) != 0 :
        customer_details.append([entry_name.get(),entry_receipt.get(),entry_item.get(),entry_quantity.get()])
        entry_name.delete(0,'end')
        entry_receipt.delete(0,'end')
        entry_item.delete(0,'end')
        entry_quantity.delete(0,'end')
        total_entries +=  1


#delete the row from the list
def delete_row ():
    global customer_details, delete_item, total_entries, name_count
    del customer_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0,'end')
    Label(main_window, text="                                           ",bg ="pink").grid(column=0,row=name_count+7)
    Label(main_window, text="                                           ",bg ="pink").grid(column=1,row=name_count+7)
    Label(main_window, text="                                           ",bg ="pink").grid(column=2,row=name_count+7)
    Label(main_window, text="                                           ",bg ="pink").grid(column=3,row=name_count+7)
    Label(main_window, text="                                           ",bg ="pink").grid(column=4,row=name_count+7)
    print_customer_details()

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


# Requirement of the input from customer
def check_input():
    global customer_details, entry_name,entry_receipt,entry_item,entry_quantity, main_window
    input_check = 0
    Label(main_window, text= "                                               ",bg ="pink").grid(column = 2, row=2,sticky =W)
    Label(main_window, text= "                                               ",bg ="pink").grid(column = 6, row=2,sticky =W)
    Label(main_window, text= "                                                         ",bg ="pink").grid(column = 2, row=3,sticky =W)
    Label(main_window, text= "                                             ",bg ="pink").grid(column = 6, row=3,sticky =W)

    # set the entry_name box not blank
    if len (entry_name.get()) == 0:
        Label(main_window, fg="red", text="Required",bg ="pink").grid(column=2, row=2,sticky =W)
        input_check = 1

     #set the entry_item box not blank
    if len (entry_item.get()) == 0:
        Label(main_window, fg="red", text="Required",bg ="pink").grid(column=6, row=2, sticky=W)
        input_check = 1
        if (entry_item.get()) == int:
             Label(main_window, fg="red", text="Required",bg ="pink").grid(column=6, row=2, sticky=W)
             input_check = 1

     #set the entry_receipt box not blank and only can use with the interger number, not accecpt text
     #Set the limit number 0 to 999999
    if (entry_receipt.get().isdigit()):
        if int(entry_receipt.get()) < 0 or int(entry_receipt.get()) > 999999:
            Label(main_window, fg="red", text="Require six interger number or less", bg="pink") .grid(column=2, row=3,sticky =W)
            input_check = 1
    else:
        Label(main_window, fg="red", text="Require six interger number or less",bg="pink") .grid(column=2, row=3,sticky =W)
        input_check = 1

   #set the entry_quantity not blank and limit number from 1 to 500
    if (entry_quantity.get().isdigit()):
        if int(entry_quantity.get()) < 1 or int(entry_quantity.get()) > 500:
            Label(main_window, fg="red", text="Quantity only 1- 500", bg="pink") .grid(column=6, row=3)
            input_check = 1
    else:
        Label(main_window, fg="red", text="Quantity only 1-500",bg="pink") .grid(column=6, row=3)
        input_check = 1


    if input_check == 0 : # if the information has used correct the input will be equal zero and the append function will be working
        append_name()


#Create the buttons and labels
def setup_buttons():
    global customer_details, entry_name,entry_receipt,entry_item,entry_quantity, total_entries, delete_item
    x = tk.StringVar()
    main_window.configure(bg= "pink")
    main_window.title("Hire Store")
    Label(main_window, text=" Hire Store", font="Times 30 italic bold",bg="Yellow").grid(row=0, column=3, sticky =E+W)
    Button(main_window, text="Quit",font="times 15 italic bold",command=quit,bg ="red",
           width=4,borderwidth=1,relief="raised", padx=2, pady=2) .grid(column=7, row=0,sticky=N)
    Button(main_window, text="Update Details",font="times 15 italic bold",command=check_input,width=11,borderwidth=11,
           relief="raised", padx=5, pady=5).grid(column=0,row=1)
    Button(main_window, text="Print Details",font="times 15 italic bold",command=print_customer_details,width=10,borderwidth=3,
           relief="raised", padx=5, pady=5) .grid(column=1,row=1)
    Label(main_window, text="Full name",bg ="pink",font="times 15 italic bold") .grid(column=0,row=2)
    entry_name = Entry(main_window)
    entry_name.grid(column=1,row=2)
    Label(main_window, text="Receipt number",bg ="pink",font="times 15 italic bold") .grid(column=0,row=3)
    entry_receipt = Entry(main_window)
    entry_receipt.grid(column=1,row=3)
    Label(main_window, text ="Type Items Or Select Items you want",
          font = "Times 10 bold", fg="red", bg="pink").grid(column = 5, row=1,sticky = E + S )
    Label(main_window, text="Item hire",bg ="pink",font="times 15 italic bold") .grid(column=4,row=2)
    entry_item = ttk.Combobox(main_window, width = 19, textvariable = x)
    entry_item ["values"] = ("Chair", "Table","Shoes","Pen","Ruler","Laptop","Ipad","Clothing","Buliding tools","Bike", "Moto Bike",
                             "Car", "Toy","Cups","Knife","Plate","Bowl")
    entry_item.grid(column =5, row =2 )
    entry_item.current()
    Label(main_window, text="Quantity",bg ="pink",font="times 15 italic bold") .grid(column=4,row=3)
    entry_quantity = Entry(main_window)
    entry_quantity.grid(column=5,row=3)
    Label(main_window, text="Row #",bg ="pink",font="times 15 italic bold") .grid(column=0,row=6)
    delete_item = Entry(main_window)
    delete_item .grid(column=1,row=6)
    Button(main_window, text="Delete",command=delete_row,font="times 15 italic bold",width=5,borderwidth=2,relief="raised",
           padx=5, pady=5) .grid(column=2,row=6,sticky =W)

#start the program running
def main():
    global main_window
    global customer_details, entry_name,entry_age,entry_gender, total_entries
    customer_details = []
    total_entries = 0
    main_window =Tk()
    setup_buttons()
    main_window.mainloop()

main()

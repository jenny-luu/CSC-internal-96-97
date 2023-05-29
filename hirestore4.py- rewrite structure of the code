from tkinter import *

#quit subroutine
def quit():
    main_window.destroy()

#print details of all the camps
def print_customer_details ():
    global j_names, total_entries, name_count
    name_count = 0
    Label(main_window, font='bold',text="Row", bg="sky blue").grid(column=0,row=7)
    Label(main_window, font='bold',text="Full name",bg ="sky blue").grid(column=1,row=7)
    Label(main_window, font='bold',text="Receipt number",bg ="sky blue").grid(column=2,row=7)
    Label(main_window, font='bold',text="Item hire",bg ="sky blue").grid(column=3,row=7)
    Label(main_window, font='bold',text="Quantity",bg ="sky blue").grid(column=4,row=7)

    while name_count < total_entries :
        Label(main_window, text=name_count,bg="sky blue").grid(column=0,row=name_count+8) 
        Label(main_window, text=(customer_details[name_count][0]),bg="sky blue").grid(column=1,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][1]),bg="sky blue").grid(column=2,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][2]),bg="sky blue").grid(column=3,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][3]),bg="sky blue").grid(column=4,row=name_count+8)
        name_count +=  1

#add the next camper to the list
def append_name ():
    global customer_details, entry_name,entry_receipt,entry_item,entry_quantity, total_entries
    if len(entry_name.get()) != 0 :
        customer_details.append([entry_name.get(),entry_receipt.get(),entry_item.get(),entry_quantity.get()])
        entry_name.delete(0,'end')
        entry_receipt.delete(0,'end')
        entry_item.delete(0,'end')
        entry_quantity.delete(0,'end')
        total_entries +=  1

#delete a row from the list
def delete_row ():
    global customer_details, delete_item, total_entries, name_count
    del customer_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0,'end')
    Label(main_window, text="       ").grid(column=0,row=name_count+7) 
    Label(main_window, text="       ").grid(column=1,row=name_count+7)
    Label(main_window, text="       ").grid(column=2,row=name_count+7)
    Label(main_window, text="       ").grid(column=3,row=name_count+7)
    Label(main_window, text="       ").grid(column=4,row=name_count+7)
    print_customer_details()

#create the buttons and labels
def setup_buttons():
    global customer_details, entry_name,entry_receipt,entry_item,entry_quantity, total_entries, delete_item
    main_window.configure(bg= "sky blue")
    main_window.title("Hire Store")
    Label(main_window, text=" Hire Store", font="Times 30 italic bold",bg="Yellow").grid(row=0, column=2, sticky =E+W)
    Button(main_window, text="Quit",font="times 15 italic bold",command=quit,bg ="sky blue") .grid(column=5, row=0,sticky=N)
    Button(main_window, text="Update Details",font="times 15 italic bold",command=append_name,width=11,borderwidth=3,
           relief="raised", padx=5, pady=5).grid(column=0,row=1)
    Button(main_window, text="Print Details",font="times 15 italic bold",command=print_customer_details,width=10,borderwidth=3,
           relief="raised", padx=5, pady=5) .grid(column=1,row=1)
    Label(main_window, text="Full name",bg ="sky blue",font="times 15 italic bold") .grid(column=0,row=2)
    entry_name = Entry(main_window)
    entry_name.grid(column=1,row=2)
    Label(main_window, text="Receipt number",bg ="sky blue",font="times 15 italic bold") .grid(column=0,row=3)
    entry_receipt = Entry(main_window)
    entry_receipt.grid(column=1,row=3)
    Label(main_window, text="Item hire",bg ="sky blue",font="times 15 italic bold") .grid(column=2,row=2)
    entry_item = Entry(main_window)
    entry_item.grid(column=3,row=2)
    Label(main_window, text="Quantity",bg ="sky blue",font="times 15 italic bold") .grid(column=2,row=3)
    entry_quantity = Entry(main_window)
    entry_quantity.grid(column=3,row=3)
    Label(main_window, text="Row #",bg ="sky blue",font="times 15 italic bold") .grid(column=0,row=6)
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


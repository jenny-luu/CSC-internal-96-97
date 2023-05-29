from tkinter import *# This code to import tkinter,so we can make a GUI


 # Create a quit function
 def quit ():
     main_window.destroy()

 #Set up buttons and Labels

 def setup_window():
     global customer_details, entry_customers, entry_item,  entry_receipt, entry_number, total_entries, entry_row
     main_window.title("Hire Store")
     Label(main_window, text=" Hire Store", font="Times 30 italic bold",bg="Yellow").grid(row=0, column=3)
     main_window.configure(bg="sky blue")
     Label(main_window,text=" Full Name",bg="sky blue").grid(column=0,row=2)
     entry_customers = Entry(main_window).grid(column=1,row=2)
     Label(main_window, text=" Item Hired",bg="Sky Blue").grid(column=0, row=3)
     entry_item=Entry(main_window).grid(column=1,row=3)
     Label(main_window,text="Receipt Number",bg="Sky Blue").grid(column=3,row=2)
     entry_receipt= Entry(main_window).grid(column=4,row=2)
     Label(main_window,text="Number Hired",bg="Sky Blue").grid(column=3,row=3)
     entry_number=Entry(main_window).grid(column=4,row=3)
     Label(main_window,text="Only type row number if you need return Items",bg="Sky Blue",fg="red",).grid(column=1,row=4,sticky=S)
     Label(main_window,text="Row#",bg="Sky Blue").grid(column=0,row=5)
     entry_row=Entry(main_window).grid(column=1,row=5)
     Button(main_window,text="Update Details",command = update_details,width=10, fg="red",bg="blue",pady=5).grid(column=4,row=4,sticky=E)
     Button(main_window,text="Print Details",command = print_customers_details,width=10,fg="red",bg="blue",pady=5).grid(column=4,row=5,sticky=E)
     Button(main_window,text="Delete",width=10,fg="red",bg="blue",pady=5).grid(column=1,row=6)
     Button(main_window, text = "Quit",command= quit, fg = "black", width=7, highlightbackground="yellow").grid(row=0, column=5,sticky=N)




 # Function for print details button
 def print_customers_details():
     global total_entries, name_count, customer_details
     name_count=0
     Label(main_window,text ="Customer Information Below", font ="Times 20 underline").grid(column=1,row=7)
     Label(main_window, text = "Row", font = "Helvetica 10 bold").grid(column=0,row=8)
     Label(main_window, text = "Customer Name",font = "Helvetica 10 bold").grid(column=1,row=8)
     Label(main_window, text = "Receipt Number",font = "Helvetica 10 bold").grid(column=2,row=8)
     Label(main_window, text = "Items Hired",font = "Helvetica 10 bold").grid(column=3,row=8)
     Label(main_window, text = "Quantity",font = "Helvetica 10 bold").grid(column=4,row=8)

     while name_count < total_entries:
         Label(main_window, text=name_count).grid(column=0, row=name_count+9)
         Label(main_window, text=(customer_details[name_count] [0])).grid(
             column=1, row=name_count+9)
         Label(main_window, text=(customer_details[name_count] [1])).grid(
             column=2, row=name_count+9)
         Label(main_window, text=(customer_details[name_count] [2])).grid(
             column=3, row=name_count+9)
         Label(main_window, text=(customer_details[name_count] [3])).grid(
             column=4, row=name_count+9)
         name_count += 1

 #Function for update button
 def update_details():
     global customer_details, entry_customers, entry_item, entry_receipt, entry_number, total_entries
     customer_details.append([entry_customers.get(), entry_item.get(), entry_receipt.get(), entry_number.get()])

     #Clear the entry boxes
     entry_customers.delete(0, 'end')
     entry_item.delete(0, 'end')
     entry_receipt.delete(0, 'end')
     entry_number.delete(0, 'end')
     total_entries += 1





 # Main function of code
 def main():
     global main_window
     global customer_detalis, total_entries
     main_window = Tk()
     setup_window()
     customer_details=[]
     total_entries = 0


 main()
print("hi")
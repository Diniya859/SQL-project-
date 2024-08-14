from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
from tkcalendar import DateEntry
from datetime import datetime

db = Database("Employee.db")
root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")
name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#535c68", padx=30, pady=30)
entries_frame.pack(side=TOP, fill=X, padx=30, pady=30)

title = Label(entries_frame, text="EMPLOYEE MANAGEMENT SYSTEM", font=("Calibri", 36, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=3, padx=10, pady=15, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
lblEmail.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lbldoj = Label(entries_frame, text="Date of Joining", font=("Calibri", 16), bg="#535c68", fg="white")
lbldoj.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtDoj = DateEntry(entries_frame, textvariable=doj, font=("Calibri", 16), width=30, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
txtDoj.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="w")

lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="w")

lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

txtAddress = Text(entries_frame, width=85, height=3, font=("Calibri", 16))
txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    email.set(row[3])
    doj.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_employee():
    if txtName.get() == "" or txtAge.get() == ""  or txtEmail.get() == "" or doj.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(1.0, END).strip() == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    
    # Convert DateEntry widget output to a string
    date_string = txtDoj.get() 
    db.insert(txtName.get(), txtAge.get(), txtEmail.get(), date_string, comboGender.get(), txtContact.get(), txtAddress.get(1.0, END).strip())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()

    

def update_employee():
    if txtName.get() == "" or txtAge.get() ==  "" or txtEmail.get() == "" or doj.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(1.0, END).strip() == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    
    date_string = txtDoj.get()  # The format will be yyyy-mm-dd
    
    db.update(row[0], txtName.get(), txtAge.get(), txtEmail.get(),date_string, comboGender.get(), txtContact.get(),
              txtAddress.get(
                  1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0, END)


btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=4, pady=4, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)


tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=1, y=500, width=1955, height=520)

# Styling the Treeview
style = ttk.Style()
style.configure("mystyle.Treeview", 
                font=('Calibri', 18), 
                rowheight=50, 
                padding=[5, 5, 5, 5])  # Padding inside cells
style.configure("mystyle.Treeview.Heading", 
                font=('Calibri', 18, 'bold'), 
                background="#dfe6e9", 
                foreground="#2d3436", 
                padding=[5, 5, 5, 5])  # Padding for headers

# Treeview Widget
tv = ttk.Treeview(tree_frame, 
                  columns=(1, 2, 3, 4, 5, 6, 7, 8), 
                  style="mystyle.Treeview")

# Headings
tv.heading("1", text="ID", anchor=CENTER)
tv.heading("2", text="Name", anchor=CENTER)
tv.heading("3", text="Age", anchor=CENTER)
tv.heading("4", text="Email", anchor=CENTER)
tv.heading("5", text="Date of Joining", anchor=CENTER)
tv.heading("6", text="Gender", anchor=CENTER)
tv.heading("7", text="Contact", anchor=CENTER)
tv.heading("8", text="Address", anchor=CENTER)

# Columns Configuration
tv.column("1", width=60, anchor=CENTER)   # Center-aligning content in the columns
tv.column("2", width=200, anchor=CENTER)
tv.column("3", width=100, anchor=CENTER)
tv.column("4", width=250, anchor=CENTER)
tv.column("5", width=180, anchor=CENTER)
tv.column("6", width=100, anchor=CENTER)
tv.column("7", width=200, anchor=CENTER)
tv.column("8", width=300, anchor=CENTER)

# Display only the headings (no tree structure)
tv['show'] = 'headings'

# Bind the selection event
tv.bind("<ButtonRelease-1>", getData)

# Packing the Treeview
tv.pack(fill=BOTH, expand=True)

# Display all records in the Treeview
dispalyAll()
root.mainloop()

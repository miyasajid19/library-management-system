from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector

def delete():
    import mysql.connector

    # Establish connection to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # <-- Enter your database password here
        database="librarymanagementsystem"
    )
    key=uid.get()
    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()
    sql=f"DELETE FROM `books` WHERE ID={key}"
    # Assuming id_entry, bookname_entry, authorname_entry, price_entry, edition_entry, genre_combobox are variables with appropriate values

    try:
        mycursor.execute(sql)
        messagebox.showinfo("Delete status","successfully deleted")
        k.destroy()
    except Exception as e:
        messagebox.showerror("Error ","Failed to update the detail of books due to "+e)

    # Commit the changes
    mydb.commit()

        # Close the cursor and database connection
    mycursor.close()
    mydb.close()

    

def getingid():
    root = Tk()
    global k
    k=root
    Label(root, text="UID ", font="ariel 10 bold").grid(row=0, column=0)
    global uid
    uid = Entry(root, width=30)
    uid.grid(row=0, column=1)
    
    Button(root, text="GO TO DELETE SECTION", bd=2, border=12, command=delete).grid(row=1, column=0, columnspan=2)
    
    root.mainloop()


getingid()
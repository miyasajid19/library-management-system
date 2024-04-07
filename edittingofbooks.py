from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector

def updatesection():
    import mysql.connector

    # Establish connection to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # <-- Enter your database password here
        database="librarymanagementsystem"
    )

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Assuming id_entry, bookname_entry, authorname_entry, price_entry, edition_entry, genre_combobox are variables with appropriate values

    
    
    if  bookname_entry_value==''or authorname_entry_value==''  or edition_entry_value=='' or genre_combobox_value=="select genre":
        messagebox.show("Error", "Blank Detectedvor genre is not selected")


        try: 
            int(price_entry_value)
        except Exception as o:
            messagebox.showerror("error","invalid Price ")

        
    else:
        # Construct the SQL query using string formatting
        sql = f"""UPDATE `books` 
                SET 
                    `ID` = '{id_entry_value}',
                    `bookname` = '{bookname_entry_value}',
                    `authorname` = '{authorname_entry_value}',
                    `price` = '{price_entry_value}',
                    `edition` = '{edition_entry_value}',
                    `genre` = '{genre_combobox_value}'
                WHERE 
                    `ID` = '{id_entry_value}';"""

        # Execute the SQL query
        try:
            mycursor.execute(sql)
            messagebox.showinfo("Update status","successfully updated")
            k.destroy()
        except Exception as e:
            messagebox.showerror("Error ","Failed to update the detail of books due to "+e)

        # Commit the changes
        mydb.commit()

        # Close the cursor and database connection
        mycursor.close()
        mydb.close()



def editthecontent():
    global k
    root = Tk()
    k=root
    root.title("Adding books")
    root.geometry("280x400")

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # <-- Enter your database password here
            database="librarymanagementsystem"
        )
        key=uid.get()
        
        mycursor = mydb.cursor()
        sql = f'SELECT `ID`, `bookname`, `authorname`, `price`, `edition`, `genre` FROM `books` WHERE ID={key};'
        mycursor.execute(sql)
        result = mycursor.fetchone()

        try:
            # Create labels and entry fields to display fetched data
            Label(root, text="ID: ").grid(row=0, column=0)
            Label(root, text="bookname: ").grid(row=1, column=0)
            Label(root, text="authorname : ").grid(row=2, column=0)
            Label(root, text="price : ").grid(row=3, column=0)
            Label(root, text="edition : ").grid(row=4, column=0)
            Label(root, text="genre : ").grid(row=5, column=0)

            global id_entry, bookname_entry, authorname_entry, price_entry, edition_entry, genre_combobox

            id_entry = Entry(root, width=30)
            id_entry.grid(row=0, column=1)
            id_entry.insert(0, result[0])
            id_entry.config(state=DISABLED)

            bookname_entry = Entry(root, width=30)
            bookname_entry.grid(row=1, column=1)
            bookname_entry.insert(0, result[1])

            authorname_entry = Entry(root, width=30)
            authorname_entry.grid(row=2, column=1)
            authorname_entry.insert(0, result[2])

            price_entry = Entry(root, width=30)
            price_entry.grid(row=3, column=1)
            price_entry.insert(0, result[3])

            edition_entry = Entry(root, width=30)
            edition_entry.grid(row=4, column=1)
            edition_entry.insert(0, result[4])

            genre_combobox = Combobox(root, values=['erotica', "children's", 'science fiction', 'young adult', 'comics', 'humor', 'adventure', 'horror', 'sports', 'memoir', 'mathematical fiction', 'programming', 'mystery', 'drama', 'cyberpunk', 'philosophy of science', 'history of science', 'historical fiction', 'crime', 'romance', 'classics', 'dystopian', 'inspirational', 'poetry', 'magical realism', 'popular science', 'paranormal', 'fantasy', 'biography', 'LGBTQ+', 'others'])
            genre_combobox.grid(row=5, column=1)
            genre_combobox.set(result[5])
            genre_combobox.config(state="readonly")
            global id_entry_value,bookname_entry_value,authorname_entry_value,edition_entry_value,price_entry_value,genre_combobox_value
            id_entry_value = id_entry.get()
            bookname_entry_value = bookname_entry.get()
            authorname_entry_value = authorname_entry.get()
            price_entry_value = price_entry.get()
            edition_entry_value = edition_entry.get()
            genre_combobox_value = genre_combobox.get()
            
            Button(root, text="update the table", width=30, command=updatesection).grid(row=6, column=0, columnspan=2)
        except Exception as e:
            messagebox.showerror("error", " no such book is detected")
            k.destroy()

    except mysql.connector.Error as e:
  
        messagebox.showerror("Error", e)
        k.destroy()

    root.mainloop()

def getingid():
    root = Tk()
    Label(root, text="UID", font="ariel 10 bold").grid(row=0, column=0)
    global uid
    uid = Entry(root, width=30)
    uid.grid(row=0, column=1)
    
    Button(root, text="GO TO UPDATE SECTION", bd=2, border=12, command=editthecontent).grid(row=1, column=0, columnspan=2)
    
    root.mainloop()


getingid()
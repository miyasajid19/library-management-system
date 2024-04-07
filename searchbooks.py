from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from database_connectter import * # Assuming connection is defined here

def filter():
    genre1 = genre.get()
    if genre1 == "All":
        # Define what should happen when the genre is "All"
        messagebox.showinfo("All Books", "Displaying all books")  # Placeholder message
    else:
        frame1.destroy()
        mycursor=connection.cursor()
        sql = f"SELECT * FROM `books` WHERE genre='{genre1}'"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        root.title("show books")
        Label(root,text="S.N.").grid(row=0,column=0,padx=20,pady=10)
        Label(root,text="ID").grid(row=0,column=1,padx=20,pady=10)
        Label(root,text="Book Name").grid(row=0,column=2,padx=20,pady=10)
        Label(root,text="Author Name").grid(row=0,column=3,padx=20,pady=10)
        Label(root,text="Price").grid(row=0,column=4,padx=20,pady=10)
        Label(root,text="Edition").grid(row=0,column=5,padx=20,pady=10)
        Label(root,text="Genre").grid(row=0,column=6,padx=20,pady=10)
        rows=1
        for x in result:
            Label(root,text=rows).grid(row=rows,column=0,padx=20,pady=10)
            Label(root,text=x[0]).grid(row=rows,column=1,padx=20,pady=10)
            Label(root,text=x[1]).grid(row=rows,column=2,padx=20,pady=10)
            Label(root,text=x[2]).grid(row=rows,column=3,padx=20,pady=10)
            Label(root,text=x[3]).grid(row=rows,column=4,padx=20,pady=10)
            Label(root,text=x[4]).grid(row=rows,column=5,padx=20,pady=10)
            Label(root,text=x[5]).grid(row=rows,column=6,padx=20,pady=10)
            rows=rows+1


root = Tk()

# This is the frame for the form
frame1 = Frame(root)
Label(frame1, text="genre").grid(row=0, column=0)
genre = Combobox(frame1, values=['erotica', 'science fiction', 'young adult', 'comics', 'humor', 'adventure', 'horror', 'sports', 'memoir', 'mathematical fiction', 'programming', 'mystery', 'drama', 'cyberpunk', 'philosophy of science', 'history of science', 'historical fiction', 'crime', 'romance', 'classics', 'dystopian', 'inspirational', 'poetry', 'magical realism', 'popular science', 'paranormal', 'fantasy', 'biography', 'LGBTQ+', 'others'])
genre.set("All")
genre.grid(row=0, column=1)
genre.config(state="readonly")
frame1.grid(row=0, column=0)
Button(frame1, text="Filter By", command=filter).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

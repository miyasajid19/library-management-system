from database_connectter import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

root=Tk()
root.title("Adding books")

root.configure(bg="#8cdadb")
root.iconbitmap(r"E:\vscode\python\PYTHON FILES\TKINTER PROJECTS\library_management_system\icons\books.ico")
def addtodatabase():
    Id=id.get()
    Bookname=bookname.get()
    Authorname=authorname.get()
    Price=price.get()
    Edition=edition.get()
    Genre=genre.get()
    if  Bookname==''or Authorname==''  or Edition=='' or Genre=="select genre":
        messagebox.showerror("Error", "Blank Detectedvor genre is not selected")
        try: 
            int(Id)
            try: 
                int(Price)
            except Exception as o:
                messagebox.showerror("error","invalid Price ")
        except Exception as o:
            messagebox.showerror("error","invalid Id")  
    else:
        try:
            import mysql.connector
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="librarymanagementsystem"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO `books`(`ID`, `bookname`, `authorname`, `price`, `edition`, `genre`) VALUES(%s, %s, %s, %s, %s, %s)"
            val = [Id,Bookname,Authorname,Price,Edition,Genre]
            try:
                mycursor.execute(sql, val)
            except Exception as p:
                messagebox.showerror("Error", p)
            mydb.commit()
            messagebox.showinfo("info","book is added to the database")
            genre.set("select genre")
            id.delete(0,END)
            bookname.delete(0,END)
            authorname.delete(0,END)
            price.delete(0,END)
            edition.delete(0,END)
        except Exception as e:
            messagebox.showerror("error",e)    
Label(root,text="ID: ",bg="#8cdadb",font="Helvetica 12 bold",fg="#f4f49e").grid(row=0,column=0)
Label(root,text="bookname: ",bg="#8cdadb",font="Helvetica 12 bold",fg="#f4f49e").grid(row=1,column=0)
Label(root,text="authorname : ",bg="#8cdadb",font="Helvetica 12 bold",fg="#f4f49e").grid(row=2,column=0)
Label(root,text="price : ",bg="#8cdadb",font="Helvetica 12 bold",fg="#f4f49e").grid(row=3,column=0)
Label(root,text="edition : ",bg="#8cdadb",font="Helvetica 12 bold",fg="#f4f49e").grid(row=4,column=0)
Label(root,text="genre : ",bg="#8cdadb",font="Helvetica 12 bold",fg="#f4f49e").grid(row=5,column=0,padx=10,pady=10)
id=Entry(root,width=30,bg="#8cdadb")
id.grid(row=0,column=1,padx=10,pady=10)
bookname=Entry(root,width=30,bg="#8cdadb")
bookname.grid(row=1,column=1,padx=10,pady=10)
authorname=Entry(root,width=30,bg="#8cdadb")
authorname.grid(row=2,column=1,padx=10,pady=10)
price=Entry(root,width=30,bg="#8cdadb")
price.grid(row=3,column=1,padx=10,pady=10)
edition=Entry(root,width=30,bg="#8cdadb")
edition.grid(row=4,column=1,padx=10,pady=10)
genre=Combobox(root,values=['erotica', 'science fiction', 'young adult', 'comics', 'humor', 'adventure', 'horror', 'sports', 'memoir', 'mathematical fiction', 'programming', 'mystery', 'drama', 'cyberpunk', 'philosophy of science', 'history of science', 'historical fiction', 'crime', 'romance', 'classics', 'dystopian', 'inspirational', 'poetry', 'magical realism', 'popular science', 'paranormal', 'fantasy', 'biography', 'LGBTQ+','others'])
genre.grid(row=5,column=1,padx=10,pady=10)
genre.set("select genre")
genre.config(state="readonly")
Button(root, text="add",width=30,command=addtodatabase,bg="#8cdadb",fg="#f4f49e").grid(row=6,column=0,columnspan=2,padx=10,pady=10)
root.mainloop()
from tkinter import *
root = Tk()
root.title("Library Management System")
root.iconbitmap(r"icons\libraryicon.ico")
root.resizable(False, False)
topframe = Frame(root)
topframe.pack(fill=X)  # Pack the top frame to fill along the x-axis
Label(topframe, text="LIBRARY MANAGEMENT SYSTEM", font="stencil 32 bold", bg="gray", fg="light green", relief=RIDGE, bd=2, border=10).pack(side=TOP, fill=X, expand=True)
# Button frame
button_frame = Frame(root)
button_frame.pack()
#functions to add books
def add():
    from addingbooks import addtodatabase
#add books
addbooks=Button(button_frame,text="Add Books",height=1,width=45,padx=10,pady=20,border=1,bd=3,bg="pink",command=add)
addbooks.grid(row=0,column=0)
#issuing of the book
def issue():
    import issuingofbooks
#issue books
issuebooks=Button(button_frame,text="Issue Books",height=1,width=45,padx=10,pady=20,border=1,bd=3,bg="pink",command=issue)
issuebooks.grid(row=0,column=1)
#editing of the books
def edit():
    from edittingofbooks import getingid
#edit books
editbooks=Button(button_frame,text="Edit Books",height=1,width=45,padx=10,pady=20,border=1,bd=3,bg="pink",command=edit)
editbooks.grid(row=1,column=0)
#returning of books
def returning():
    import returnningofbooks
#return books
returnbooks=Button(button_frame,text="Return Books",height=1,width=45,padx=10,pady=20,border=1,bd=3,bg="pink",command=returning)
returnbooks.grid(row=1,column=1)
#deleting of books
def delete():
    from deletingthebook import getingid
#delete books
deletebooks=Button(button_frame,text="Delete Books",height=1,width=45,padx=10,pady=20,border=1,bd=3,bg="pink",command=delete)
deletebooks.grid(row=2,column=0)
#showing of books
def show():
    import showbooks
#show books
showbooks=Button(button_frame,text="Show Books",height=1,width=45,padx=10,pady=20,border=1,bd=3,bg="pink",command=show)
showbooks.grid(row=2,column=1)
#searching of books
def search():
    import searchbooks
#search books
searchbooks=Button(button_frame,text="Search Books",height=1,width=45,padx=10,pady=20,border=1,bd=3,bg="pink",command=search)
searchbooks.grid(row=3,column=0)
#loging out of books
def logout():
    root.destroy()
#log out
logout=Button(button_frame,text="Log Out",height=1,width=45,padx=10,pady=20,border=1,bd=3,bg="pink",command=logout)
logout.grid(row=3,column=1)
root.mainloop()

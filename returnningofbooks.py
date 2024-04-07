from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from database_connectter import *
root=Tk()
from datetime import datetime, timedelta


def display():

    mycursor = connection.cursor()
    studentquery = f'SELECT `student_id`, `first_name`, `last_name`, `email`, `branch`, `contact`, `hostel`, `enrolled_year` FROM `students` WHERE student_id={uid};'
    mycursor.execute(studentquery)
    
    student = mycursor.fetchone()
    print("student data fetched")
    mycursor = connection.cursor()
    bookquery = f'SELECT `ID`, `bookname`, `authorname`, `price`, `edition`, `genre` FROM `books` WHERE ID={bid};'
    mycursor.execute(bookquery)
    
    book = mycursor.fetchone()
    print("book data fetched")
    

    issuedbookquery = f'SELECT `bookid`, `studentid`, `issueddate`, `returndate`, `retain`, `fine` FROM `issuedbooks` WHERE bookid={bid};'
    mycursor.execute(issuedbookquery)
    
    issuedbook = mycursor.fetchone()
    print("issuedbook is fetched")
    root=Tk()
    root.title("Issuing of the books ")
    root.resizable(False,False)
    frame1=Frame(root)
    Label(frame1,text="Student details ",bd=3,border=5,font="stencil 20 bold",padx=10,pady=10).grid(row=0,column=1)
    Label(frame1,text=" registration number : ",padx=10,pady=10).grid(row=1,column=0)
    Label(frame1,text=" first name : ",padx=10,pady=10).grid(row=2,column=0)
    Label(frame1,text="Last Name : ",padx=10,pady=10).grid(row=3,column=0)
    Label(frame1,text="Official Email : ",padx=10,pady=10).grid(row=4,column=0)
    Label(frame1,text="Branch : ",padx=10,pady=10).grid(row=5,column=0)
    Label(frame1,text="COntact Details : ",padx=10,pady=10).grid(row=6,column=0)
    Label(frame1,text="Address : ",padx=10,pady=10).grid(row=7,column=0)
    Label(frame1,text="Date of joining : ",padx=10,pady=10).grid(row=8,column=0)
    
    Label(frame1,text=student[0],padx=10,pady=10).grid(row=1,column=1)
    Label(frame1,text=student[1],padx=10,pady=10).grid(row=2,column=1)
    Label(frame1,text=student[2],padx=10,pady=10).grid(row=3,column=1)
    Label(frame1,text=student[3],padx=10,pady=10).grid(row=4,column=1)
    Label(frame1,text=student[4],padx=10,pady=10).grid(row=5,column=1)
    Label(frame1,text=student[5],padx=10,pady=10).grid(row=6,column=1)
    Label(frame1,text=student[6],padx=10,pady=10).grid(row=7,column=1)
    Label(frame1,text=student[7],padx=10,pady=10).grid(row=8,column=1)

    frame1.grid(row=0,column=0)
    frame2=Frame(root)
    
    Label(frame2,text="Book  details ",bd=3,border=5,font="stencil 20 bold",padx=10,pady=10).grid(row=0,column=1)
    Label(frame2,text=" Book ID : ",padx=10,pady=10).grid(row=1,column=0)
    Label(frame2,text=" Book Name : ",padx=10,pady=10).grid(row=2,column=0)
    Label(frame2,text=" Author name : ",padx=10,pady=10).grid(row=3,column=0)
    Label(frame2,text="Price : ",padx=10,pady=10).grid(row=4,column=0)
    Label(frame2,text="Genre : ",padx=10,pady=10).grid(row=5,column=0)
    Label(frame2,text="Edition : ",padx=10,pady=10).grid(row=6,column=0)


    
    Label(frame2,text=book[0],padx=10,pady=10).grid(row=1,column=1)
    Label(frame2,text=book[1],padx=10,pady=10).grid(row=2,column=1)
    Label(frame2,text=book[2],padx=10,pady=10).grid(row=3,column=1)
    Label(frame2,text=book[3],padx=10,pady=10).grid(row=4,column=1)
    Label(frame2,text=book[4],padx=10,pady=10).grid(row=5,column=1)
    Label(frame2,text=book[5],padx=10,pady=10).grid(row=6,column=1)
    frame2.grid(row=0,column=1)
    frame3=Frame(root)
    import datetime
    Label(frame3,text="Issue the book").grid(row=0,column=0)
    Label(frame3,text="issued date").grid(row=1,column=0)
    ent=Entry(frame3, width=30)
    global current_date_str,return_date_str
    current_date = issuedbook[2]
    current_date_str = current_date.strftime("%Y-%m-%d")
    ent.insert(0, current_date_str)
    ent.config()
    ent.grid(row=1, column=1)
    
    Label(frame3,text="Return date").grid(row=2,column=0)
    ret=Entry(frame3, width=30)
    return_date = issuedbook[3]
    return_date_str = return_date.strftime("%Y-%m-%d")
    ret.insert(0, return_date_str)
    ret.config()
    ret.grid(row=2, column=1)
    # Inside the sajid() function
    
    def sajid():
        messagebox.showinfo("info","is due clear???")
        from datetime import datetime
        return_date = issuedbook[3] + timedelta(days=15)
        print(return_date)
        ret.delete(0, END)  # Clear the Entry widget before inserting the new value
        ret.insert(0, return_date)
        ret.config(state="readonly")
        print(return_date)
        ent.delete(0, END)
        ent.insert(0, issuedbook[3])
        ent.config(state="readonly")
        ent.grid(row=1, column=1)
        print(type(issuedbook[3]))
        issued_date = ent.get()  # Assuming ent is an input field or variable containing the issued date
        return_date = ret.get()
        date_object = datetime.strptime(return_date, '%Y-%m-%d').date()
        print("Type of return_date:", type(date_object))
        print(issued_date,'\n',return_date)
        mycursor = connection.cursor()
        query = f"UPDATE issuedbooks SET issueddate='{issued_date}', returndate='{return_date}', retain='Yes' WHERE bookid={bid};"
        print(issued_date,'\n sdf',return_date_str)
        print(query)
        try:
            mycursor.execute(query)
            connection.commit()
            messagebox.showinfo("Update status", "Successfully updated")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        import sys
        sys.exit()
       


# Button to trigger sajid()
    Button(frame3, text="Retain the book", bd=5, border=10, command=sajid).grid(row=3, column=0, columnspan=2)
    def miya():
        messagebox.showinfo("info","is due clear???")
        mycursor = connection.cursor()
        query = f"DELETE FROM `issuedbooks` WHERE bookid={bid};"
        
        print(query)
        try:
            mycursor.execute(query)
            connection.commit()
            messagebox.showinfo("Update status", "Successfully delected")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
    Button(frame3,text="Return the book",bd=5,border=10,command=miya).grid(row=3,column=2,columnspan=2)
    frame3.grid(row=2,column=0)
    print(return_date)
    currentdate=datetime.date.today()
    late=(currentdate-return_date).days
    Label(frame1,text="Fine/Dues ",padx=10,pady=10).grid(row=9,column=0)
    
    if late<=0:
        Label(frame1,text=0,padx=10,pady=10).grid(row=9,column=1)
    else:
        Label(frame1,text=late*5,padx=10,pady=10).grid(row=9,column=1)
    
    root.mainloop()
def getbookinfo():
    bookid=id.get()
    mycursor = connection.cursor()
    sql = 'SELECT * FROM issuedbooks'
    mycursor.execute(sql)
    global uid,bid
    book = mycursor.fetchall()
    for index, value in enumerate(book):
        if int(bookid)==value[0]:
            uid=value[1]
            bid=value[0]
            display()
            break
        else: 
            pass
    
Label(root,text="Book ID : ").grid(row=0,column=0)
id=Entry(root,width=30)
id.grid(row=0,column=1)
Button(root, text="Check",bd=3,border=3,width=30,padx=10,pady=10,command=getbookinfo).grid(row=1, column=0, columnspan=2)
root.mainloop()
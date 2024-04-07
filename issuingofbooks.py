from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from database_connectter import *
def sendmail():
    # Access global variables
    global student
    print(student[3])
    # Retrieve subject and body from widgets
    global book

    import smtplib as s

    server = s.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        # Use the application-specific password generated from your Google Account
        server.login('your mail', 'your password')
    except Exception as e:
        print(e)
    subjecttext='Regarding Issuance of Book'
    body=f'''
Dear {student[1]+' '+student[2]},

I hope this email finds you well. I am writing to inform you about the issuance of a book from our library. The details are as follows:

Book ID: {book[0]}
Book Title: {book[1]}
Genre: {book[5]}
Issue Date: {current_date_str}
Return Due Date: {return_date_str}
Please ensure that the book is returned by the specified due date. If you have any questions or need further assistance, feel free to reach out to me.

Thank you for your cooperation.

Sincerely,

place your details


    '''
    message = f"Subject: {subjecttext}\n\n{body}"

    try:
        server.sendmail('your mail',student[3], message)
        messagebox.showinfo("info","Successfully mail was sent")
    except Exception as e:
        messagebox.showerror("error",f"error in sending mail due to {e}")

    server.quit()
def issued():
    print(current_date_str,'\n',return_date_str)
    mycursor = connection.cursor()
    sql = "INSERT INTO `issuedbooks`(`bookid`, `studentid`, `issueddate`, `returndate`, `retain`, `fine`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = [book[0], student[0], current_date_str, return_date_str, 'No', 0]

    print(val)
    try:
        mycursor.execute(sql, val)
        messagebox.showinfo("info","book issued")
        sendmail()
        root.destroy()
    except Exception as p:
        messagebox.showerror("Error", p)
    connection.commit()
def issuebook():
    root=Tk()
    root.title("Issuing of the books ")
    root.geometry("800x500+100+100")
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
    Label(frame3,text="current date").grid(row=1,column=0)
    ent=Entry(frame3, width=30)
    global current_date_str,return_date_str
    current_date = datetime.date.today()
    current_date_str = current_date.strftime("%Y-%m-%d")
    ent.insert(0, current_date_str)
    ent.config(state="disabled")
    ent.grid(row=1, column=1)
    
    Label(frame3,text="Return date").grid(row=2,column=0)
    ret=Entry(frame3, width=30)
    return_date = datetime.date.today()+ datetime.timedelta(days=30)
    return_date_str = return_date.strftime("%Y-%m-%d")
    ret.insert(0, return_date_str)
    ret.config(state="disabled")
    ret.grid(row=2, column=1)
    Button(frame3,text="Issue the book",bd=5,border=10,command=issued).grid(row=3,column=0,columnspan=2)
    frame3.grid(row=2,column=0)
    root.mainloop()
def checkbook(book_id):
    mycursor = connection.cursor()
    sql = 'SELECT * FROM books'
    mycursor.execute(sql)
    global book
    book = mycursor.fetchall()
    for index,value in enumerate(book):
        
        if value[0]==book_id:
            book=book[index]
            issuebook()
            break
        else:
            print(value[0])
            print("index not found")
            

def getbookinfo():
    root = Toplevel()
    root.title("Issuing of books")
    root.resizable(False, False)
    Label(root, text="Enter book Id : ").grid(row=0, column=0)
    book_id_entry = Entry(root, width=30)  # Use a different variable name
    book_id_entry.grid(row=0, column=1)

    Button(root, text="Get details", command=lambda: checkbook(int(book_id_entry.get())),bd=3, border=10).grid(row=1, column=0, columnspan=2)

    root.mainloop()


def checkstudent():
    student_id = int(id_entry.get())
    mycursor = connection.cursor()
    sql = 'SELECT * FROM students'
    mycursor.execute(sql)
    global student
    student = mycursor.fetchall()
    uids = list()
    for x in student:
        uids.append(x[0])

    if student_id in uids:
        for index,value in enumerate(uids):
            
            if student_id==value:
                
                messagebox.showinfo("info", "Data fetched successfully")
                student=student[index]
                
                getbookinfo()
                
    else:
        messagebox.showerror("info", "Failed to fetch data")

root = Tk()
k = root
root.title("Issuing of books")
root.resizable(False, False)

Label(root, text="Enter student Id : ").grid(row=0, column=0)
id_entry = Entry(root, width=30)
id_entry.grid(row=0, column=1)

Button(root, text="Get student details", command=checkstudent, bd=3, border=10).grid(row=1, column=0, columnspan=2)

root.mainloop()
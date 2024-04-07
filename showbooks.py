from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
from database_connectter import *
import mysql.connector

root = Tk()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the size and position of the window
window_width = int(screen_width * 0.8)  # Set the window width to 80% of screen width
window_height = int(screen_height * 0.8)  # Set the window height to 80% of screen height
x_position = int((screen_width - window_width) / 2)  # Center the window horizontally
y_position = int((screen_height - window_height) / 2)  # Center the window vertically
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

mycursor = connection.cursor()
sql = 'SELECT * FROM `books` ORDER BY `books`.`ID` ASC '
mycursor.execute(sql)
result = mycursor.fetchall()

root.title("Show Books")

# Create a Treeview widget to display data in tabular format
tree = Treeview(root, columns=("S.N.", "ID", "Book Name", "Author Name", "Price", "Edition", "Genre"), show="headings")
tree.pack(fill="both", expand=True)

# Add headings for the columns
tree.heading("S.N.", text="S.N.", anchor="center")
tree.heading("ID", text="ID", anchor="center")
tree.heading("Book Name", text="Book Name", anchor="center")
tree.heading("Author Name", text="Author Name", anchor="center")
tree.heading("Price", text="Price", anchor="center")
tree.heading("Edition", text="Edition", anchor="center")
tree.heading("Genre", text="Genre", anchor="center")

# Add data to the Treeview
for i, x in enumerate(result, start=1):
    tree.insert("", "end", values=(i, x[0], x[1], x[2], x[3], x[4], x[5]))

# Center align all the columns
for col in tree["columns"]:
    tree.column(col, anchor="center")

# Add scrollbar to the Treeview
scrollbar = Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.pack(side=RIGHT, fill=Y)
tree.configure(yscrollcommand=scrollbar.set)

root.mainloop()

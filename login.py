import sqlite3
from tkinter import *
import tkinter.messagebox as msg

window = Tk()
window.geometry('900x600')
reg_image = PhotoImage(file='registerbg.png')
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
window.title("Medicine Management System")

# Heading
TopHeadingFrame = Frame(window, width=700, bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLabel = Label(TopHeadingFrame, text='Medicine Management System - login', font=('Helvetica', 24), fg='red', bg='black')
HeadingLabel.grid(row=1, column=0, padx=10, pady=10)
MidFrame = Frame(window, width=600, bd=1)
MidFrame.pack(side=TOP)  # Fixed typo here

# Username
username = StringVar()
username.set('')
usernameLabel = Label(MidFrame, text='username', font=('Helvetica', 16), fg='yellow', bg='black')
usernameLabel.grid(row=0, column=0, padx=10, pady=10)
usernameTextBox = Entry(MidFrame, font=('Helvetica', 16), textvariable=username)
usernameTextBox.grid(row=0, column=1, padx=10, pady=10)

# Password
password = StringVar()
password.set('')
passwordLabel = Label(MidFrame, text='password', font=('Helvetica', 16), fg='yellow', bg='black')
passwordLabel.grid(row=1, column=0, padx=10, pady=10)
passwordTextBox = Entry(MidFrame, font=('Helvetica', 16), textvariable=password, show='*')  # Added show='*' here
passwordTextBox.grid(row=1, column=1, padx=10, pady=10)

def register():
    window.destroy()
    import register

def login():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM 'userdata' WHERE UserName = ? AND Password = ?""", (username.get(), password.get()))
    if len(list(cursor.fetchall())) > 0:
        msg.showinfo('Login confirmation', 'Login successful', icon='info')
        window.destroy()
        import home
    else:
        msg.showinfo('Login Error', 'User not defined', icon='warning')

# Submit button
submit_btn = Button(MidFrame, text='Register', command=register, font=('Helvetica', 18), fg='black', bg='green')
submit_btn.grid(row=3, column=1, padx=10, pady=10)

# Already user label
NotUserLabel = Label(MidFrame, text='Not a user yet?', font=('Helvetica', 16), fg='yellow', bg='black')
NotUserLabel.grid(row=3, column=0, padx=10, pady=10)

# Login button
login_btn = Button(MidFrame, text='Login', command=login, font=('Helvetica', 18), fg='black', bg='blue')
login_btn.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()

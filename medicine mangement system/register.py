from tkinter import *

import sqlite3
import tkinter.messagebox as msg

window = Tk()
window.geometry('900x600')
reg_image = PhotoImage(file='registerbg.png')
bg_label = Label(window,image=reg_image)
window.title("Medicine Management System")

#heading
TopHeadingFrame = Frame(window, width=700,bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLabel = Label(TopHeadingFrame,text='Medicine Management System - Register',font=('Helvetica',24),fg='red',bg='black')
HeadingLabel.grid(row=1,column=0,padx=10,pady=10)
MidFrame = Frame(window,width=600,bd=1)
MidFrame.pack(sid=TOP)

conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()
cursor.execute("""create table if not exists 'userdata' 
(Name text, ID int, UserName text,Password text , Mobile_no text,Email text)""")
conn.commit()

#name
name = StringVar()
name.set('')
NameLabel = Label(MidFrame,text='Name',font=('Helvetica',16),fg='yellow',bg='black')
NameLabel.grid(row=0,column=0,padx=10,pady=10)
NameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=name)
NameTextBox .grid(row=0,column=1,padx=10,pady=10)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

#id
id = IntVar()
id.set('')
idLabel = Label(MidFrame,text='ID',font=('Helvetica',16),fg='yellow',bg='black')
idLabel.grid(row=1,column=0,padx=10,pady=10)
idTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=id)
idTextBox .grid(row=1,column=1,padx=10,pady=10)

#username
username= StringVar()
username.set('')
usernameLabel = Label(MidFrame,text='username',font=('Helvetica',16),fg='yellow',bg='black')
usernameLabel.grid(row=2,column=0,padx=10,pady=10)
usernameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=username)
usernameTextBox .grid(row=2,column=1,padx=10,pady=10)

#password
password= StringVar()
password.set('')
passwordLabel = Label(MidFrame,text='password',font=('Helvetica',16),fg='yellow',bg='black')
passwordLabel.grid(row=3,column=0,padx=10,pady=10)
passwordTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=password)
passwordTextBox .grid(row=3,column=1,padx=10,pady=10)

#mobile_no
mobile_no= StringVar()
mobile_no.set('')
mobile_noLabel = Label(MidFrame,text='mobile no',font=('Helvetica',16),fg='yellow',bg='black')
mobile_noLabel.grid(row=4,column=0,padx=10,pady=10)
mobile_noTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=mobile_no)
mobile_noTextBox .grid(row=4,column=1,padx=10,pady=10)

#email
email = StringVar()
email.set('')
emailLabel = Label(MidFrame,text='email',font=('Helvetica',16),fg='yellow',bg='black')
emailLabel.grid(row=5,column=0,padx=10,pady=10)
emailTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=email)
emailTextBox .grid(row=5,column=1,padx=10,pady=10)

def register():
    conn = sqlite3.connect('.venv/medicine.db')
    cursor = conn.cursor()
    cursor.execute("""insert into 'userdata' (Name,ID,UserName,Password,Mobile_no,Email) values(?,?,?,?,?,?)""",
                   (str(name.get()),str(id.get()),str(username.get()),str(password.get()),str(mobile_no.get()),str(email.get())))
    conn.commit()
    if cursor.rowcount>0:
        msg.showinfo('Confirmation','New user added',icon='info')
    else:
        msg.showinfo('Error','New user noy added',icon='warning')

def login():
    window.destroy()
    import login

#submit button
submit_btn = Button(MidFrame,text='Submit',command=register,font=('Helvetica',18),fg='black',bg='green')
submit_btn.grid(row=6,column=1,padx=10,pady=10)

#Alreadyuserlabel
AlreadyUserLabel = Label(MidFrame,text='already a user?',font=('Helvetica',16),fg='yellow',bg='black')
AlreadyUserLabel.grid(row=7,column=0,padx=10,pady=10)

#login button
login_btn = Button(MidFrame,text='Login',command=login,font=('Helvetica',18),fg='black',bg='blue')
login_btn.grid(row=7,column=1,padx=10,pady=10)

window.mainloop()

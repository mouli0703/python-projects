import sqlite3
from tkinter import *
import tkinter.messagebox as msg

window = Tk()
window.geometry('900x600')
reg_image = PhotoImage(file='registerbg.png')
bg_label = Label(window,image=reg_image)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)
window.title("Medicine Management System")
window.iconbitmap('icon.ico')


#heading
TopHeadingFrame = Frame(window, width=700,bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLabel = Label(TopHeadingFrame,text='Medicine Management System - home',font=('Helvetica',24),fg='red',bg='black')
HeadingLabel.grid(row=1,column=0,padx=10,pady=10)
MidFrame = Frame(window, width=600, bd=1)
MidFrame.pack(side=TOP)

#btns
def add():
    window.destroy()
    import add_medicine
def view():
    window.destroy()
    import view_medicine
def search():
    window.destroy()
    import search_medicine
def delete():
    window.destroy()
    import delete_medicine
def logout():
    window.destroy()
    import login


#add btn
add_btn = Button(MidFrame, text='ADD MEDICINE', command=add, font=('Helvetica', 18), fg='black', bg='blue')
add_btn.grid(row=0, column=1, padx=10, pady=10)

#view btn
view_btn = Button(MidFrame, text='VIEW MEDICINE', command=view, font=('Helvetica', 18), fg='black', bg='blue')
view_btn.grid(row=1, column=1, padx=10, pady=10)

#search btn
search_btn = Button(MidFrame, text='SEARCH MEDICINE', command=search, font=('Helvetica', 18), fg='black', bg='blue')
search_btn.grid(row=2, column=1, padx=10, pady=10)

#delete btn
delete_btn = Button(MidFrame, text='DELETE MEDICINE', command=delete, font=('Helvetica', 18), fg='black', bg='blue')
delete_btn.grid(row=3, column=1, padx=10, pady=10)

#logout btn
login_btn = Button(MidFrame, text='LOGOUT', command=logout, font=('Helvetica', 18), fg='black', bg='green')
login_btn.grid(row=4, column=1, padx=10, pady=10)





window.mainloop()
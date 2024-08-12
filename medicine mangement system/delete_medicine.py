import sqlite3
from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk

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
HeadingLabel = Label(TopHeadingFrame,text='Medicine Management System - delete',font=('Helvetica',24),fg='red',bg='black')
HeadingLabel.grid(row=1,column=0,padx=10,pady=10)

MidFrame = Frame(window,width=700,bd=1)
MidFrame.pack(sid=TOP)

medicine_name = StringVar()
medicine_name.set('')
medicine_NameLabel = Label(MidFrame,text='Name',font=('Helvetica',16),fg='yellow',bg='black')
medicine_NameLabel.grid(row=1,column=0,padx=10,pady=10)
medicine_NameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=medicine_name)
medicine_NameTextBox .grid(row=1,column=1,padx=10,pady=10)

view_frame = Frame(window,bd=1)
view_frame.pack(side=TOP,fill=X)


tv = ttk.Treeview(view_frame,columns=('MedicineName' , 'MedicineID' ,'Brand' ,'ChemicalComponent' ,'MFG_Date' ,'EXP_Date','price' ))
tv.heading('#1',text='MedicineName')
tv.heading('#2',text='MedicineID')
tv.heading('#3',text='Brand')
tv.heading('#4',text='ChemComp')
tv.heading('#5',text='MFG')
tv.heading('#6',text='EXP')
tv.heading('#7',text='Price')

tv.column('#0',width=0,stretch=NO)
tv.column('#1',width=50)
tv.column('#2',width=50)
tv.column('#3',width=50)
tv.column('#4',width=50)
tv.column('#5',width=50)
tv.column('#6',width=50)
tv.column('#7',width=50)
tv.pack(fill=X)



def back():
    window.destroy()
    import home


def delete():
    for i in tv.get_children():
        tv.delete(i)

    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    medname = str(medicine_name.get())

    # Check if the medicine exists
    cursor.execute("SELECT * FROM medicine WHERE MedicineName = ?", (medname,))
    data = cursor.fetchone()

    if data:
        cursor.execute("DELETE FROM medicine WHERE MedicineName = ?", (medname,))
        conn.commit()
        msg.showinfo('Confirm Message', 'Medicine deleted successfully', icon='info')
    else:
        msg.showinfo('Error Message', 'Medicine not found', icon='warning')

    cursor.close()
    conn.close()



def view():
    for i in tv.get_children():
        tv.delete(i)

    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute("select * from 'medicine' ")
    data = cursor.fetchall()
    for i in data:
        tv.insert("", 'end', values=i)

    cursor.close()
    conn.commit()



delete_btn = Button(MidFrame,text='delete',command=delete,font=('Helvetica',18),fg='black',bg='red')
delete_btn.grid(row=1,column=2,padx=10,pady=10)

view_btn = Button(MidFrame,text='view',command=view,font=('Helvetica',18),fg='black',bg='red')
view_btn.grid(row=1,column=3,padx=10,pady=10)
#login button
back_btn = Button(MidFrame,text='Back',command=back,font=('Helvetica',18),fg='black',bg='red')
back_btn.grid(row=1,column=4,padx=10,pady=10)



window.mainloop()
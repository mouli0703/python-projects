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
HeadingLabel = Label(TopHeadingFrame,text='Medicine Management System - add',font=('Helvetica',24),fg='red',bg='black')
HeadingLabel.grid(row=1,column=0,padx=10,pady=10)
MidFrame = Frame(window,width=600,bd=1)
MidFrame.pack(sid=TOP)

conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()
cursor.execute("""create table if not exists 'medicine' 
(MedicineName text, MedicineID int,Brand text,ChemicalComponent text,MFG_Date text,EXP_Date text,price int)""")
conn.commit()

#name
medicine_name = StringVar()
medicine_name.set('')
medicine_NameLabel = Label(MidFrame,text='Name',font=('Helvetica',16),fg='yellow',bg='black')
medicine_NameLabel.grid(row=0,column=0,padx=10,pady=10)
medicine_NameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=medicine_name)
medicine_NameTextBox .grid(row=0,column=1,padx=10,pady=10)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

#id
medicine_id = IntVar()
medicine_id.set('')
medicine_idLabel = Label(MidFrame,text='Medicine ID',font=('Helvetica',16),fg='yellow',bg='black')
medicine_idLabel.grid(row=1,column=0,padx=10,pady=10)
medicine_idTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=medicine_id)
medicine_idTextBox .grid(row=1,column=1,padx=10,pady=10)

#brand
brandname= StringVar()
brandname.set('')
brandnameLabel = Label(MidFrame,text='brand name',font=('Helvetica',16),fg='yellow',bg='black')
brandnameLabel.grid(row=2,column=0,padx=10,pady=10)
brandnameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=brandname)
brandnameTextBox .grid(row=2,column=1,padx=10,pady=10)

#chemical_component
chemical_component= StringVar()
chemical_component.set('')
chemical_componentLabel = Label(MidFrame,text='Chemical_Component',font=('Helvetica',16),fg='yellow',bg='black')
chemical_componentLabel.grid(row=3,column=0,padx=10,pady=10)
chemical_componentTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=chemical_component)
chemical_componentTextBox .grid(row=3,column=1,padx=10,pady=10)

#mfg_date
mfg= StringVar()
mfg.set('')
mfgLabel = Label(MidFrame,text='MFG_Date',font=('Helvetica',16),fg='yellow',bg='black')
mfgLabel.grid(row=4,column=0,padx=10,pady=10)
mfgTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=mfg)
mfgTextBox .grid(row=4,column=1,padx=10,pady=10)

#exp_date
exp= StringVar()
exp.set('')
expLabel = Label(MidFrame,text='EXP_Date',font=('Helvetica',16),fg='yellow',bg='black')
expLabel.grid(row=5,column=0,padx=10,pady=10)
expTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=exp)
expTextBox .grid(row=5,column=1,padx=10,pady=10)

#price
price= IntVar()
price.set('')
priceLabel = Label(MidFrame,text='Price',font=('Helvetica',16),fg='yellow',bg='black')
priceLabel.grid(row=6,column=0,padx=10,pady=10)
priceTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=price)
priceTextBox .grid(row=6,column=1,padx=10,pady=10)

def add():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute("""insert into 'medicine' (MedicineName , MedicineID ,Brand ,ChemicalComponent ,MFG_Date ,EXP_Date,price ) values(?,?,?,?,?,?,?)""",
                   (str(medicine_name.get()),str(medicine_id.get()),str(brandname.get()),str(chemical_component.get()),str(mfg.get()),str(exp.get()),str(price.get())))
    conn.commit()
    if cursor.rowcount>0:
        msg.showinfo('ADD MEDICINE','New Medicine added',icon='info')
    else:
        msg.showinfo('Error','New Medicine not added',icon='warning')

def logout():
    window.destroy()
    import login

def back():
    window.destroy()
    import home

#submit button
add_btn = Button(MidFrame,text='ADD',command=add,font=('Helvetica',18),fg='black',bg='green')
add_btn.grid(row=7,column=1,padx=10,pady=10)


#login button
back_btn = Button(MidFrame,text='Back',command=back,font=('Helvetica',18),fg='black',bg='blue')
back_btn.grid(row=8,column=1,padx=10,pady=10)


window.mainloop()

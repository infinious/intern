
from tkinter import *
import tkinter.messagebox
window =Tk()
window.title("Registration form")
window.geometry('400x400')
window.configure(background = "gold")
label_1=Label(window,text= "employe resgistration form",font=("bold, 29")).grid(row= 0,column= 2)
firstname = Label(window, text = "first name", width=20,font=("bold, 10")).grid(row= 1,column= 1)
lastname = Label(window,text = "lastname",width=20,font=("bold, 10")).grid(row= 2,column= 1)
address = Label(window,text = "address",width=20,font=("bold, 10")).grid(row= 3,column= 1)
state1= Entry(window).grid(row = 5, column =2)
postal1= Entry(window).grid(row = 6, column =2)
Email1= Entry(window).grid(row = 9, column =2)
Mobile1= Entry(window). grid(row = 8, column =2)
choose1= Entry(window).grid(row = 11, column =2)
def onClick():
    tkinter.messagebox.showinfo("welcome","your details submitted succesfully !")
    Button(window,text="submit", command=onClick,width=20,bg='brown' ,fg='white').grid(row = 14,column = 6)
    window.mainloop()
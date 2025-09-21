#start

from tkinter import *
from tkinter import messagebox
import mysql.connector

def LoginForm():
    Myform = Tk()
    Myform.geometry('400x300')
    Myform.configure(bg = 'cornflower blue')
    Myform.title('Login Form')
    Myform.resizable(False, False)
    Label(Myform, text = 'LOGIN', fg = 'black', bg = "cornflower blue", font = ('Bahnschrift bold', 30)).place(x=145, y=20)
    Label(Myform, text = 'User Name', fg = 'black', bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=52, y=98)
    Label(Myform, text = 'Password', fg = 'black', bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=52, y=148)
    v1 = StringVar()
    v2 = StringVar()
    T1 = Entry(Myform, textvariable = v1, font = ('bahnschrift semibold', 10)).place(x=202, y=110)
    T2 = Entry(Myform, textvariable = v2, show = "*",font = ('bahnschrift semibold', 10)).place(x=202, y=160)
    Button(Myform, text = "Close", command = Myform.destroy, border = 3, font = ("bahnschrift semibold", 15), bg = "gray26", fg = "white", padx = 15).place(x=42, y=220)
    def CLEAR():
        v1.set('')
        v2.set('')
    Button(Myform,text = "Clear", command = CLEAR, border = 3, font = ("bahnschrift semibold", 15), bg = "gray26", fg = "white", padx = 15).place(x=152, y=220)
    def VALIDATE():
        if v1.get() == "abhiraj" and v2.get() == "1809":
            messagebox.showinfo("Login Success", "You are a valid user")
        else:
            messagebox.showinfo("Login Failure", "Please try again")
    Button(Myform, text = "Login", command = VALIDATE, border = 3, font = ("bahnschrift semibold", 15), bg = "gray26", fg = "white", padx = 15).place(x=262, y=220)
    Myform.mainloop()

LoginForm()

#end
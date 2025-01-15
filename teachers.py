from tkinter import*
##from tkinter import messagebox
##from tkinter import ttk
import sqlite3
class teacherpanel:
    def __init__(self):
        self.w=Tk()
        l=Label(text='Name')
        l.pack()
        self.e=Entry()
        self.e.pack()
        l1=Label(text='Email')
        l1.pack()
        self.e1=Entry()
        self.e1.pack()
        l2=Label(text='Password')
        l2.pack()
        self.e2=Entry()
        self.e2.pack()
        l3=Label(text='Branch')
        l3.pack()
        self.e3=Entry()
        self.e3.pack()
        b1=Button(text='login',command=self.login1)
        b1.pack()

    def login1(self):
        db=sqlite3.connect('attn.db')
        cr=db.cursor()
        cr.execute(f'''select* from teacher where email='{self.e1.get()}' and password='{self.e2.get()}' ''')
        data=cr.fetchone()
        print('login')
##        if data:
##            self.x.destroy()
##            self.m=Tk()
##            l=Label(text="Hello"+data[0])
##            l.pack()
##            cr.execute(f'''select* from student where branch='{data[3]}' ''')
##            student=cr.fetchone()
##            lb=Listbox()
##            lb.pack()
##            for i in range(0,len(stuednt)):
##                lb.insert(student[i][0])
##        else:
##            messagebox.showinfo('failure','Wrong Creadentials')
##        print("Login")

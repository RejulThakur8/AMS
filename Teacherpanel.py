from tkinter import*
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
class TeacherPanel:
    def __init__(self):
        self.a=Tk()
        self.img=PhotoImage(file=r'C:\Users\HP\Pictures\Screenshots\T5.png')
        l=Label(text='',image=self.img)
        l.place(x=0,y=0)
        l1=Label(text="Email")
        l1.pack()
        self.e1=Entry()
        self.e1.pack()
        l2=Label(text="Password")
        l2.pack()
        self.e2=Entry()
        self.e2.pack()
        b=Button(text="Login",command=self.login1)
        b.pack()
        self.a.geometry("500x500")
    def data_update(self):
        db=sqlite3.connect('attendance_system.db')
        cr=db.cursor()
        cr.execute(f"update teacher set name='{self.e.get()}', password='{self.e2.get()}', email='{self.e1.get()}'")
        db.commit()
        
    def login1(self):
        db=sqlite3.connect('attendance_system.db')
        cr=db.cursor()
        cr.execute(f'''select* from Teacher WHERE email='{self.e1.get()}' and password='{self.e2.get()}' ''')
        data=cr.fetchone()
        print(data)
        if data:
            self.a.destroy()
            self.y=Tk()
            l=Label(text='Hi' +data[0])
            l.pack()
            notebook=ttk.Notebook()
            frame1=Frame(self.y,bg="orange",padx=300,pady=200)
            date=datetime.now().date()
            db=sqlite3.connect('attendance_system.db')
            cr=db.cursor()
            cr.execute('''select* from student where branch='CSE' ''')
            data=cr.fetchall()
            def check():
                cr.execute(f'''select* from Attendance where date='{date}' ''')
                marked=cr.fetchall()
                if(len(marked)!=0):
                   print("already marked")
                else:
                    for i in range(len(data)):
                        if d[i].get()==1:
                            cr.execute(f'''insert into Attendance values('{date}',{data[i][4]},'Present') ''')
                            db.commit()
                        else:
                            cr.execute(f'''insert into Attendance values('{date}',{data[i][4]},'Absent') ''')
                            db.commit()

            d=[]
            c=[]
            l=[]
            l1=[]
            for i in range(len(data)):
                l.append(Label(frame1,text=data[i][0]))
                l[i].grid(row=i,column=0)
                l1.append(Label(frame1,text=data[i][4]))
                l1[i].grid(row=i,column=1)
                d.append(IntVar())
                c.append(Checkbutton(frame1,variable=d[i],onvalue=1,offvalue=0,text="Present"))
                c[i].grid(row=i,column=2)
            b=Button(frame1,text="Mark Attendance",command=check)
            b.grid(row=len(data),column=1)
##            tree=ttk.Treeview(frame1,column=("Name","Rollno","Branch"))
##            tree.heading("Name",text="Name")
##            tree.heading("Rollno",text="Rollno")9
##            tree.heading("Branch",text="Branch")
##            cr.execute(f'''select* from student where branch='{data[3]}' ''')
##            student=cr.fetchall()
##            print(student)
##            tree.pack()
##            for i in range(0,len(student)):
##                tree.insert("","end",values=(student[i][0],student[i][4],student[i][3]))
            frame1.pack()
        
            frame2=Frame(self.y,bg="red",padx=100,pady=200)
            l=Label(frame2,text="Name")
            l.pack()
            self.e=Entry(frame2)
            self.e.pack()
            l1=Label(frame2,text="email")
            l1.pack()
            self.e1=Entry(frame2)
            self.e1.pack()
            l2=Label(frame2,text="Password")
            l2.pack()
            self.e2=Entry(frame2)
            self.e2.pack()
            b=Button(frame2,text="update",command=self.data_update)
            b.pack()
            frame2.pack()
            notebook.add(frame1,text="Attendance")
            notebook.add(frame2,text="Profile")
            notebook.pack()
            '''cr.execute(f"select*from student where branch='{data[3]}'")
            student=cr.fetchall()
            
            for i in range(0,len(student)):
                    notebook.insert(i,student[1][0])'''

                            
        else:
            messagebox.showinfo('failure','Wrong Creadentials')



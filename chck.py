 ##from tkinter import*
##r=Tk()
##def check():
##    print(d.get())
##d=IntVar()
##c=Checkbutton(variable=d,onvalue=1,offvalue=0,text='hi')
##c.pack()
##
##b=Button(text='check',command=check)
##b.pack()

###############
##from tkinter import*
##r=Tk()
##def check():
##    for i in range(5):
##        if d[i].get()==1:
##            print(e[i])
##d=[]
##c=[]
##e=["Music","Dancing","Playing","traveling","Fighting"]
##for i in range(5):
##    d.append(IntVar())
##    c.append(Checkbutton(variable=d[i],onvalue=1,offvalue=0,text=e[i]))
##    c[i].pack()
##
##b=Button(text="check",command=check)
##b.pack()

###############################
from tkinter import*
import sqlite3
from datetime import datetime
date=datetime.now().date()
db=sqlite3.connect('attendance_system.db')
cr=db.cursor()
cr.execute('''select * from student where branch='CSE' ''')
data=cr.fetchall()
r=Tk()
def check():
    cr.execute(f'''select * from Attendance where date='{date}' ''')
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
    l.append(Label(text=data[i][0]))
    l[i].grid(row=i,column=0)
    l1.append(Label(text=data[i][4]))
    l1[i].grid(row=i,column=1)
    d.append(IntVar())
    c.append(Checkbutton(variable=d[i],onvalue=1,offvalue=0,text="Present"))
    c[i].grid(row=i,column=2)
b=Button(text="Mark Attendance",command=check)
b.grid(row=len(data),column=1)




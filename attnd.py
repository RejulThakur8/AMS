import sqlite3
db=sqlite3.connect('attendance_System.db')
cr=db.cursor()
cr.execute('''Create table Teacher(Name varchar(32),Email varchar(32),Password varchar(32),Branch varchar(32))''');
cr.execute('''Create table Student(Name varchar(32),Email varchar(32),Password varchar(32),Branch varchar(32),Rollno int(32),Date Date)''');
cr.execute('''Create table Attendance(Date Date, Rollno int(32),attendance varchar(32))''');
db.commit()

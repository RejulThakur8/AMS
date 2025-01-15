from tkinter import*
from Teacherpanel import*
from Studentpanel import*
from tkinter import ttk
window=Tk()
img=PhotoImage(file=r'C:/Users/HP/OneDrive/Pictures/Screenshots/T2.png')
l=Label(text='',image=img)
l.pack(expand=True,fill="both")
'''notebook=ttk.Notebook(window)
frame=Frame(window,bg="#a26aea",padx=50,pady=70)
frame.pack() 
frame1=Frame(window,bg="#c9184a",padx=50,pady=70)
frame1.pack()
notebook.add(frame,text='teacher pannel')
notebook.add(frame1,text='student pannel')
notebook.pack(expand=True,fill="both")'''
def Teacher():
    window.destroy()
    t=TeacherPanel()
def Student():
    window.destroy()
    s=StudentPanel()
    
    
b=Button(l,text='teacher panel',command=Teacher,height=2,width=18,bg="#f7aef8",highlightthickness=0)
b.place(relx=0.5,rely=0.5)
b1=Button(l,text='student panel',command=Student,height=2,width=18,bg="#f7aef8",highlightthickness=0)
b1.place(relx=0.5,rely=0.6)
window.geometry("500x500")
#window.maxsize(width=500,height=500)#expand to max size according to given height and width
##window.attributes("-fullscreen",True)#expand to full screen but for minimizing we have to use esc
mainloop()


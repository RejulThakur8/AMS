from tkinter import*
from teachers import*   ###file name
from St import*
window=Tk()


def teacher():
    print("Welcome")
    window.destroy()
    t=teacherpanel()   ####class name
def student():
    print("Thank You")
    window.destroy()
    s=studentpanel()
b=Button(window,text='teacherpanel',command=teacher)
b.pack()
b1=Button(window,text='StudentPanel',command=student)
b1.pack()
mainloop()

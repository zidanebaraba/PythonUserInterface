from tkinter import *
from tkinter import ttk

def BuClick(id):
    print("ID : {}".format(id))

root=Tk()

ttk.Button(root,text="Click Me 1",command=lambda :BuClick(10)).pack()


root.mainloop()
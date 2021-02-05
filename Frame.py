from tkinter import *
from tkinter import ttk

root=Tk()

frame=ttk.Frame(root)
frame.pack()
frame.config(height=200, width=200,relief=RIDGE, padding=10)
ttk.Button(frame, text="Hallo 1").grid(row=0,column=0)
ttk.Button(frame, text="Hallo 1").grid(row=0,column=3)

frame2=ttk.Frame(root)
frame2.pack()
frame2.config(height=200, width=200, relief=RIDGE, padding=(10,10))
ttk.Button(frame2, text="Hallo Pack 1").pack()
ttk.Button(frame2, text="Hallo Pack 2").pack()

ttk.LabelFrame(height=100,width=100,text="Third Frame").pack()
root.mainloop()
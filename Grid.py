from tkinter import *
from tkinter import ttk

root=Tk()

ttk.Label(root,text="green",background="green").grid(row=0,column=0,padx=5,pady=5, sticky='snew')
ttk.Label(root,text="blue",background="blue").grid(row=0,column=1,ipadx=5,ipady=5, sticky='snew')
ttk.Label(root,text="red",background="red").grid(row=0,column=2,rowspan=2, sticky='snew')
ttk.Label(root,text="white",background="white").grid(row=1,column=0,columnspan=2,sticky='snew')

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)

root.mainloop()
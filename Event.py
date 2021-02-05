from tkinter import *
from tkinter import ttk

root=Tk()

def key_press(event):
    print("type : {}".format(event.type))
    
def button_press(event):
    print("Button is Pressed")

bu=ttk.Button(root,text="Click Here")
bu.pack()
bu1=ttk.Button(root,text="click 2")
bu1.pack()

bu.bind("<ButtonPress>",button_press)
root.bind("<Control-c>",key_press)

style=ttk.Style()
style.theme_use('classic')
style.configure('TButton',foreground='red',font=('arial',24))
style.configure('Info.TButton',foreground='black',font=('calibri',18))
style.map('Info.TButton',background=[('pressed','blue')])

bu1.configure(style='Info.TButton')

root.mainloop()
from tkinter import *
from tkinter import ttk

# Mengabil file import
root=Tk() 

# Edit Style
style=ttk.Style()
style.configure('TButton', foreground='green', font=('arial',18))

#Membuat Input dibawah tombol
entry=ttk.Entry(root,width=50)
entry.pack()

# Membuat Tombol
button=ttk.Button(root,text="click me") 
button.pack() 

# Masukan Logo
logo=PhotoImage(file="login.gif")
button.config(image=logo,compound=LEFT)
Resize_Logo=logo.subsample(10,10)
button.config(image=Resize_Logo)

def BuClick():
    print(entry.get())
    entry.delete(0,END)

button.config(command=BuClick)

# Melihat GUI
root.mainloop() 
import tkinter as tk
from tkinter import *
import os 


#attach things to this to effect the app as a whole
root = tk.Tk()
root.geometry('400x200')
root.configure(background="teal")

def button_command():
    eg = e.get()
    fg = f.get()
    gg = g.get()

    hg = eg.replace(fg,gg)

    e.delete(0, END)
    f.delete(0, END)
    g.delete(0, END)
    root.clipboard_clear()
    root.clipboard_append(hg)
    print(hg)

    e.insert(0, "Result Is")
    f.insert(0, "In Your")
    g.insert(0, "Clipboard")
    
    return None


#title
root.title("DROmie Tools 1")
Label(root, text="List Demessifier", bg="#add8e6", font="none 35 bold").pack()

#text box
e = Entry(root)
e.place(width=150,height=150)
e.insert(END,"Enter List Here")
e.pack()

#text box2
f = Entry(root, width = 20)
f.insert(END,"What Do U Want Replaced?")
f.pack()

#text box2
g = Entry(root, width = 20)
g.insert(END,"Replace with...")
g.pack()


#button 
b = Button(root, text = "Submit", command = button_command,)
b.pack()


root.mainloop()


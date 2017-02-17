# -*- coding: utf8 -*-
import tkinter
from tkinter.constants import *

# set main window
tk = tkinter.Tk()
tk.title(u"Hello World!")
tk.geometry("400x300")

# build frame
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)

# make a lebel
label = tkinter.Label(frame, text="Hello, World", font=("Courier",30))
label.pack(fill=X, expand=1)

# set a button
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)

tk.mainloop()

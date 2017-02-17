# -*- coding: utf8 -*-
import tkinter as tk
import sys


### set main window
root = tk.Tk()
root.title(u"Tkinter Test")
root.geometry("400x300")

# set label
buff = tk.StringVar()
buff.set("Please press a button")
label = tk.Label(root,textvariable=buff)
label.pack()
#label.place(x=150, y=200)

# reset text of label 
def make_cmd(n):
	return lambda : buff.set('button %d pressed' % n)

# set button
for x in range(4):
	button = tk.Button(root,text="Button %d" % x, command=make_cmd(x))
	button.pack(fill='both')

root.mainloop()

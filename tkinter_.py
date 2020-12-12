#import tkinter
#me = tkinter.Tk()
#me.title("Testing tkinter program")

#a = tkinter.Label(me, text = "Hello December")
#a.pack()
#me.mainloop()

from tkinter import *

me = Tk()
me.title("Hello")

var = StringVar()
a = Label(me, textvariable = var, relief= RAISED)
var.set("Hello December")
a.pack()
me.mainloop()
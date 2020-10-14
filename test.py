from tkinter import *

root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
text=label.cget("text")
num=len(text)
print(text[6:num])
label.pack()
root.mainloop()
import tkinter as tk

HEIGHT = 600
WIDTH = 800

root =tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff') # 80c1ff hex for blue hex
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight= 0.8)

button = tk.Button(frame, text = "Text button")
button.pack()

label = tk.Label(frame, text="This is a label", bg='yellow')
label.pack()

entry = tk.Entry(frame, bg='green')
entry.pack()

root.mainloop() 
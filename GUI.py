import tkinter as tk

HEIGHT = 600
WIDTH = 800

root =tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff') # 80c1ff hex for blue hex
frame.place(relx = 0.1, rely = 0.1,relwidth = 0.8,relheight = 0.8)

label = tk.Label(frame, text="Username: ", bg='yellow')
label.place(relx = 0.44, rely = 0.4, relwidth = 0.13, relheight = 0.05)

label = tk.Label(frame, text="Password:  ", bg='yellow')
label.place(relx = 0.44, rely = 0.46, relwidth = 0.13, relheight = 0.05)

entry = tk.Entry(frame, bg='green')
entry.place(relx = 0.58, rely = 0.4, relwidth = 0.15, relheight = 0.05)

entry = tk.Entry(frame, bg='green')
entry.place(relx = 0.58, rely = 0.46, relwidth = 0.15, relheight = 0.05)

button = tk.Button(frame, text = "Enter")
button.place(relx = 0.61, rely = 0.52, relwidth = 0.12, relheight = 0.05)

root.mainloop() 
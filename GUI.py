import tkinter as tk
from PIL import Image, ImageTk, ImageOps 
import tkinter.font as tkFont
import sqlite3

HEIGHT = 600
WIDTH = 1000

root =tk.Tk()
root.title('Heart Pacemaker')
root.geometry("1000x600")
#background_image = ImageTk.PhotoImage(Image.open("image/Background.jpg"))

background_image = Image.open("image/Background.jpg")
background_image = ImageOps.fit(background_image, (1000, 600))
background_image = ImageTk.PhotoImage(background_image)

<<<<<<< Updated upstream
frame = tk.Frame(root, bg='#80c1ff') # 80c1ff hex for blue hex
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight= 0.8)

button = tk.Button(frame, text = "Text button")
button.pack()

label = tk.Label(frame, text="This is a label", bg='yellow')
label.pack()

entry = tk.Entry(frame, bg='green')
entry.pack()
=======
background_label =  tk.Label(root, image = background_image)
background_label.place(x = 0, y = 0,relwidth = 1, relheight = 1)


#b = tk.Button(root, text="My Text", image=background_image, relief="flat", state="normal", command = root.quit)
#b.pack()

#canvas_list = [front, password, register] 



def frame1():
	Start.place_forget()
	canvas_front.place(x = 100, y = 50)
	Pacemaker_sign.place_forget()

def Reg():
	canvas_front.place_forget()
	canvas_reg.place(x = 300, y = 50)

def reg_back():
	canvas_reg.place_forget()
	canvas_front.place(x = 100, y = 50)

def log_back():
	canvas_log.place_forget()
	canvas_front.place(x = 100, y = 50)

def log(user_number):
	canvas_front.place_forget()
	canvas_log.place(x = 300, y = 50)



fontStyle = tkFont.Font(family="Blackadder ITC", size=25)
fontStyle2 = tkFont.Font(family="Times New Roman", size=10)

# Databases
# Create a username database
Data = sqlite3.connect('Users.db')

c = Data.cursor()#data cursor
'''
#create database for the first time commented after
c.execute("""CREATE TABLE address(
		username text,
		password text)
	""")
'''

Data.commit()

Data.close()



#Starting Page:
canvas_front = tk.Canvas(root, height = HEIGHT-100, width = WIDTH-200, bg = "#80aaff")

Pacemaker_sign=tk.Label(root, text = "Pacemaker Interface", font = fontStyle,bg = "#3333ff", fg = "#ffff80")
Pacemaker_sign.place(relx = 0.1, rely = 0.15)

Start = tk.Button(root, text = "Start", command = frame1)
Start.place(relx = 0.8, rely=0.15)



#Front page front canvas
User1 = tk.Button(canvas_front, text = "User: ", width = 20, height = 2, font = fontStyle2,command = lambda: log(0))
User2 = tk.Button(canvas_front, text = "User: ", width = 20, height = 2, font = fontStyle2,command = lambda: log(1))
User3 = tk.Button(canvas_front, text = "User: ", width = 20, height = 2, font = fontStyle2,command = lambda: log(2))
User4 = tk.Button(canvas_front, text = "User: ", width = 20, height = 2, font = fontStyle2,command = lambda: log(3))
User5 = tk.Button(canvas_front, text = "User: ", width = 20, height = 2, font = fontStyle2,command = lambda: log(4))
User6 = tk.Button(canvas_front, text = "User: ", width = 20, height = 2, font = fontStyle2,command = lambda: log(5))
User7 = tk.Button(canvas_front, text = "User: ", width = 20, height = 2, font = fontStyle2,command = lambda: log(6))
User8 = tk.Button(canvas_front, text = "User: ", width = 20, height = 2, font = fontStyle2,command = lambda: log(7))
User9 = tk.Button(canvas_front, text = "User: ", width = 20, height = 2, font = fontStyle2,command = lambda: log(8))
User10 = tk.Button(canvas_front, text = "User: ", width = 20, height = 2, font = fontStyle2,command = lambda: log(9))
Register = tk.Button(canvas_front, text = "Register", command = Reg)

User1.place(relx = 0.1, rely = 0.15)
User2.place(relx = 0.6, rely = 0.15)
User3.place(relx = 0.1, rely = 0.3)
User4.place(relx = 0.6, rely = 0.3)
User5.place(relx = 0.1, rely = 0.45)
User6.place(relx = 0.6, rely = 0.45)
User7.place(relx = 0.1, rely = 0.6)
User8.place(relx = 0.6, rely = 0.6)
User9.place(relx = 0.1, rely = 0.75)
User10.place(relx = 0.6, rely = 0.75)
Register.place(relx =0.9,rely = 0.9)


#Register canvas
canvas_reg = tk.Canvas(root, height = 500, width = 400, bg = "#80aaff")

submit_button = tk.Button(canvas_reg, text = "Submit")
back_button = tk.Button(canvas_reg, text = "Back", command = reg_back)
username_label=tk.Label(canvas_reg, text = "Username: ",font = tkFont.Font(family="Blackadder ITC", size=15), bg = "#80aaff", fg = "#990000")
username_entry=tk.Entry(canvas_reg,font= fontStyle2)
password_label=tk.Label(canvas_reg, text = "Password: ",font = tkFont.Font(family="Blackadder ITC", size=15), bg = "#80aaff", fg = "#990000")
password_entry=tk.Entry(canvas_reg,font= fontStyle2)


submit_button.place(relx = 0.8, rely = 0.9)
back_button.place(relx = 0.2, rely = 0.9)
username_label.place(relx = 0.25, rely = 0.38)
username_entry.place(relx = 0.45,rely = 0.4, relwidth = 0.3)
password_label.place(relx = 0.25, rely = 0.48)
password_entry.place(relx = 0.45,rely = 0.5, relwidth = 0.3)


#Log in Canvas
canvas_log = tk.Canvas(root, height = 500, width = 400, bg = "#80aaff")

submit_button2 = tk.Button(canvas_log, text = "Submit")
back_button2 = tk.Button(canvas_log, text = "Back", command = log_back)
username_label2 = tk.Label(canvas_log, text = "Username: ",font = tkFont.Font(family="Blackadder ITC", size=15), bg = "#80aaff", fg = "#990000")
password_label2=tk.Label(canvas_log, text = "Password: ",font = tkFont.Font(family="Blackadder ITC", size=15), bg = "#80aaff", fg = "#990000")
password_entry2=tk.Entry(canvas_log,font= fontStyle2)


submit_button2.place(relx = 0.8, rely = 0.9)
back_button2.place(relx = 0.2, rely = 0.9)
username_label2.place(relx = 0.25, rely = 0.38)
password_label2.place(relx = 0.25, rely = 0.48)
password_entry2.place(relx = 0.45,rely = 0.5, relwidth = 0.3)

>>>>>>> Stashed changes

root.mainloop() 
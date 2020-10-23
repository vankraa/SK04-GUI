from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageOps 
import tkinter.font as tkFont
import sqlite3

HEIGHT = 600   #dimension of the starting window
WIDTH = 1000   #dimension of the starting window
USER_ON = None        #Indicate which user is logged in
CANVAS_BACKGROUND_COLOR = "#80aaff"


root =tk.Tk()
root.title('Heart Pacemaker')
root.geometry("1100x600")


#Background image
class Background(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open("image/Background.jpg")
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)


e = Background(root)
e.pack(fill=BOTH, expand=YES)

#Images required
start_image = Image.open("image/Start.png")
start_image = ImageTk.PhotoImage(start_image)

reg_image = Image.open("image/Register.png")
reg_image = ImageTk.PhotoImage(reg_image)

back_image = Image.open("image/Backward.png")
back_image = ImageTk.PhotoImage(back_image)

del_image = Image.open("image/delete.png")
del_image = ImageTk.PhotoImage(del_image)

#inital username/passwords
USERNAME = ["---"]*10
PASSWORD = []
OID = [None]*10
Error_text = ""


Data = sqlite3.connect('Users.db')
c = Data.cursor()#data cursor

#fetch all of the data in database
c.execute("SELECT *, oid FROM address")
records = c.fetchall()

num = len(records)

USERNAME.clear()
PASSWORD.clear()
OID.clear()
for x in records:
	USERNAME.append(x[0])
	PASSWORD.append(x[1])
	OID.append(str(x[2]))

for x in range(10-num):
	USERNAME.append("---")
	OID.append("")

Data.commit()

Data.close()
global canvas_front


def frame1():
	Start.place_forget()
	canvas_reg.place_forget()
	canvas_log.place_forget()
	canvas_front.place(x = 150, y = 50)
	Pacemaker_sign.place_forget()


	Data = sqlite3.connect('Users.db')

	c = Data.cursor()#data cursor

	#fetch all of the data in database
	c.execute("SELECT *, oid FROM address")
	records = c.fetchall()
	num = len(records)

	USERNAME.clear()
	PASSWORD.clear()
	OID.clear()
	for x in records:
		USERNAME.append(x[0])
		PASSWORD.append(x[1])
		OID.append(str(x[2]))

	for x in range(10-num):
		USERNAME.append("---")
		OID.append("")

	User1.configure(text = "User: " + USERNAME[0])
	User2.configure(text = "User: " + USERNAME[1])
	User3.configure(text = "User: " + USERNAME[2])
	User4.configure(text = "User: " + USERNAME[3])
	User5.configure(text = "User: " + USERNAME[4])
	User6.configure(text = "User: " + USERNAME[5])
	User7.configure(text = "User: " + USERNAME[6])
	User8.configure(text = "User: " + USERNAME[7])
	User9.configure(text = "User: " + USERNAME[8])
	User10.configure(text = "User: " + USERNAME[9])

	Data.commit()

	Data.close()



def log(user_number):
	global username_label2
	canvas_front.place_forget()
	canvas_log.place(x = 350, y = 50)
	
	global USER_ON
	USER_ON = user_number
	username_label2.configure(text = "Username:  " + USERNAME[user_number])



def delete_user(user_num):
	Data = sqlite3.connect('Users.db')

	c = Data.cursor()#data cursor

	#Delete a record from database
	if(OID[user_num] != ""):
		c.execute("DELETE from address WHERE oid ="+ OID[user_num])

	Data.commit()

	Data.close()
	frame1()

def Reg():
	canvas_front.place_forget()
	canvas_reg.place(x = 350, y = 50)

def reg_username_password():
	Data = sqlite3.connect('Users.db')

	c = Data.cursor()#data cursor

	#write into the data base
	if(username_entry.get()!= "" and password_entry.get()!= "" and len(PASSWORD)<10):
		c.execute("INSERT INTO address VALUES (:username, :password)",
				{
					'username': username_entry.get(),
					'password': password_entry.get()
				}
			)

	Data.commit()

	Data.close()

	username_entry.delete(0,END)
	password_entry.delete(0,END)

	frame1()

def program_frame():
	text = password_entry2.get()
	password_entry2.delete(0,END) 					#Clear the entry
	if(text == PASSWORD[USER_ON]):					#Check if the password entered is correct
		canvas_interface.place(x = 50, y = 25)
		canvas_log.place_forget()
	else:
		pass_wrong = tk.Label(canvas_log, text = "Wrong Password, please try again!", font = fontStyle2 ,bg = CANVAS_BACKGROUND_COLOR)
		pass_wrong.place(relx = 0.26,rely = 0.55)


fontStyle = tkFont.Font(family="Blackadder ITC", size=25)
fontStyle2 = tkFont.Font(family="Times New Roman", size=10)
fontStyle3 = tkFont.Font(family="Blackadder ITC", size=15)

# Databases
# Create a username database
'''
Data = sqlite3.connect('Users.db')

c = Data.cursor()#data cursor

#create database for the first time commented after
c.execute("""CREATE TABLE address(
		username text,
		password text)
	""")

Data.commit()

Data.close()
'''

#Starting Page:
Pacemaker_sign=tk.Label(root, text = "Pacemaker Interface", font = fontStyle,bg = "#3333ff", fg = "#ffff80")
Pacemaker_sign.place(relx = 0.1, rely = 0.15)

Start = tk.Button(root, image = start_image, command = frame1)
Start.place(relx = 0.76, rely=0.5)



#Front page front canvas
canvas_front = tk.Canvas(root, height = HEIGHT-100, width = WIDTH-200, bg = CANVAS_BACKGROUND_COLOR)

User1 = tk.Button(canvas_front, text = "User: " + USERNAME[0], width = 30, height = 2, font = fontStyle2,command = lambda: log(0))
User2 = tk.Button(canvas_front, text = "User: " + USERNAME[1], width = 30, height = 2, font = fontStyle2,command = lambda: log(1))
User3 = tk.Button(canvas_front, text = "User: " + USERNAME[2], width = 30, height = 2, font = fontStyle2,command = lambda: log(2))
User4 = tk.Button(canvas_front, text = "User: " + USERNAME[3], width = 30, height = 2, font = fontStyle2,command = lambda: log(3))
User5 = tk.Button(canvas_front, text = "User: " + USERNAME[4], width = 30, height = 2, font = fontStyle2,command = lambda: log(4))
User6 = tk.Button(canvas_front, text = "User: " + USERNAME[5], width = 30, height = 2, font = fontStyle2,command = lambda: log(5))
User7 = tk.Button(canvas_front, text = "User: " + USERNAME[6], width = 30, height = 2, font = fontStyle2,command = lambda: log(6))
User8 = tk.Button(canvas_front, text = "User: " + USERNAME[7], width = 30, height = 2, font = fontStyle2,command = lambda: log(7))
User9 = tk.Button(canvas_front, text = "User: " + USERNAME[8], width = 30, height = 2, font = fontStyle2,command = lambda: log(8))
User10 = tk.Button(canvas_front, text = "User: " + USERNAME[9], width = 30, height = 2, font = fontStyle2,command = lambda: log(9))

u1_del = tk.Button(canvas_front, image = del_image,command = lambda: delete_user(0))
u2_de2 = tk.Button(canvas_front, image = del_image,command = lambda: delete_user(1))
u3_de3 = tk.Button(canvas_front, image = del_image,command = lambda: delete_user(2))
u4_de4 = tk.Button(canvas_front, image = del_image,command = lambda: delete_user(3))
u5_de5 = tk.Button(canvas_front, image = del_image,command = lambda: delete_user(4))
u6_de6 = tk.Button(canvas_front, image = del_image,command = lambda: delete_user(5))
u7_de7 = tk.Button(canvas_front, image = del_image,command = lambda: delete_user(6))
u8_de8 = tk.Button(canvas_front, image = del_image,command = lambda: delete_user(7))
u9_de9 = tk.Button(canvas_front, image = del_image,command = lambda: delete_user(8))
u10_del0 = tk.Button(canvas_front, image = del_image,command = lambda: delete_user(9))

Register = tk.Button(canvas_front, image = reg_image, command = Reg)

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

u1_del.place(relx = 0.38, rely = 0.16)
u2_de2.place(relx = 0.88, rely = 0.16)
u3_de3.place(relx = 0.38, rely = 0.31)
u4_de4.place(relx = 0.88, rely = 0.31)
u5_de5.place(relx = 0.38, rely = 0.46)
u6_de6.place(relx = 0.88, rely = 0.46)
u7_de7.place(relx = 0.38, rely = 0.61)
u8_de8.place(relx = 0.88, rely = 0.61)
u9_de9.place(relx = 0.38, rely = 0.76)
u10_del0.place(relx = 0.88, rely = 0.76)

Register.place(relx =0.82,rely = 0.87)


#Register canvas
canvas_reg = tk.Canvas(root, height = 500, width = 400, bg = CANVAS_BACKGROUND_COLOR)

submit_button = tk.Button(canvas_reg, text = "Submit", command = reg_username_password)
back_button = tk.Button(canvas_reg, image= back_image, command = frame1)
username_label=tk.Label(canvas_reg, text = "Username: ",font = fontStyle3, bg = CANVAS_BACKGROUND_COLOR, fg = "#990000")
username_entry=tk.Entry(canvas_reg,font= fontStyle2)
password_label=tk.Label(canvas_reg, text = "Password: ",font = fontStyle3, bg = CANVAS_BACKGROUND_COLOR, fg = "#990000")
password_entry=tk.Entry(canvas_reg,font= fontStyle2)


submit_button.place(relx = 0.8, rely = 0.9)
back_button.place(relx = 0.2, rely = 0.88)
username_label.place(relx = 0.25, rely = 0.38)
username_entry.place(relx = 0.45,rely = 0.4, relwidth = 0.3)
password_label.place(relx = 0.25, rely = 0.48)
password_entry.place(relx = 0.45,rely = 0.5, relwidth = 0.3)


#Log in Canvas
canvas_log = tk.Canvas(root, height = 500, width = 400, bg = CANVAS_BACKGROUND_COLOR)

submit_button2 = tk.Button(canvas_log, text = "Submit", command = program_frame)
back_button2 = tk.Button(canvas_log, image= back_image, command = frame1)
password_label2=tk.Label(canvas_log, text = "Password: ",font = tkFont.Font(family="Blackadder ITC", size=15), bg = CANVAS_BACKGROUND_COLOR, fg = "#990000")
password_entry2=tk.Entry(canvas_log,font= fontStyle2)
username_label2 = tk.Label(canvas_log, text = "Username:  ",font = fontStyle3, bg = CANVAS_BACKGROUND_COLOR, fg = "#990000")

submit_button2.place(relx = 0.8, rely = 0.9)
back_button2.place(relx = 0.2, rely = 0.88)
password_label2.place(relx = 0.25, rely = 0.48)
password_entry2.place(relx = 0.45,rely = 0.5, relwidth = 0.3)
username_label2.place(relx = 0.25, rely = 0.38)



#USER INTERFACE CANVAS
canvas_interface = tk.Canvas(root, height = HEIGHT-50, width = WIDTH, bg = CANVAS_BACKGROUND_COLOR)
AOO_mode = tk.Button(canvas_interface, text = "AOO", font = fontStyle3, bg = CANVAS_BACKGROUND_COLOR, fg = "#990000")
VOO_mode = tk.Button(canvas_interface, text = "VOO", font = fontStyle3, bg = CANVAS_BACKGROUND_COLOR, fg = "#990000")
AAI_mode = tk.Button(canvas_interface, text = "AAI", font = fontStyle3, bg = CANVAS_BACKGROUND_COLOR, fg = "#990000")
VVI_mode = tk.Button(canvas_interface, text = "VVI", font = fontStyle3, bg = CANVAS_BACKGROUND_COLOR, fg = "#990000")
connected = canvas_interface.create_oval(10,10,20,20,fill = "red")
connected_label = tk.Label(canvas_interface, text = "Connected", font = tkFont.Font(family="Blackadder ITC", size=10), bg = CANVAS_BACKGROUND_COLOR, fg = "#990000")
Error_label = tk.Label(canvas_interface, text = "Error"+Error_text, font = tkFont.Font(family="Blackadder ITC", size=10), bg = CANVAS_BACKGROUND_COLOR, fg = "#990000"))

AOO_mode.place(rely = 0.05, relx = 0.1)
VOO_mode.place(rely = 0.05, relx = 0.35)
AAI_mode.place(rely = 0.05, relx = 0.6)
VVI_mode.place(rely = 0.05, relx = 0.85)
connected_label.place(rely = 0.008, relx = 0.025)

root.mainloop() 
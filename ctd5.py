import hashlib
from tkinter import *
import re
from tkinter import messagebox

r = Tk()
r.geometry("700x700")
r.title('                       LOGIN  ')

password='Super'
hash1 = hashlib.md5(password.encode("utf-8")).hexdigest()

def loginfun():
    user=username.get()
    Pass=password.get()
    
    hash2 = hashlib.md5(Pass.encode("utf-8")).hexdigest()
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    
    
    if (user == "guest" and hash2 == hash1):
        messagebox.showinfo("message", "Right!")
    elif regex.search(user)!= None or regex.search(Pass)!= None:
        messagebox.showinfo("message", "donot use special characters")
    elif user=="" or Pass=="":
        messagebox.showinfo("message", "Please enter a username or password")
    else :
        messagebox.showinfo("message", "wrong password or username,TRY AGAIN")


Label(r, text='Username:',font="bold").grid(row=0)
Label(r, text='Password:',font="bold").grid(row=1)
username= Entry(r)
password= Entry(r)
username.grid(row=0, column=1)
password.grid(row=1, column=1)
password.config(show = '*')

button = Button(r, text='login', width=20,fg ="green",command=loginfun).place(x=240,y= 200)

r.mainloop()
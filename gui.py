# tkinter

import tkinter as tk
import pymysql as mysql
from tkinter import messagebox,ttk
from PIL import Image, ImageTk

def sp(pg):
    pg.tkraise()

def register():
    name = rg_name.get()
    phone = rg_phone.get()
    email = rg_email.get()
    password = rg_pass.get()

    if not all([name,phone,email,password]):
        messagebox.showwarning("Field warning","Fill All Fields")
        return None

    if len(phone) != 10:
        messagebox.showwarning("Field warning","Phone Number should be 10 Digits")
        return None

    try:
        db = mysql.connect(user="root",password="root",host="localhost",database="swarna_tech",port=3306)
        cur = db.cursor()
        cur.execute("""insert into users(name,email,phone,password) values(%s,%s,%s,%s)""",(name,email,phone,password))
        db.commit()
        db.close()
        messagebox.showinfo("Registered Successfully","Successfully Registered")
    except Exception as e:
        messagebox.showerror("Registered Error",e)

def login():
    email = lg_email.get()
    password = lg_pass.get()

    if not all([email,password]):
        messagebox.showwarning("Field warning","Fill All Fields")
        return None

    try:
        db = mysql.connect(user="root",password="root",host="localhost",database="swarna_tech",port=3306)
        cur = db.cursor()
        cur.execute(""" select * from users where email = %s and password = %s """,(email,password))
        if cur.fetchone():
            messagebox.showinfo("Login Successfully","Successfully Login👍👍")
            dg.tkraise()
        else:
            messagebox.showerror("Login Error","Login Failed")
        db.commit()
        db.close()
    except Exception as e:
        messagebox.showerror("Login Error",e)









main = tk.Tk() #like wooden frame
main.geometry("1920x1080")
main.config(background="gray")
tk.Label(main,text="Hello Python Guys..",bg="gray",fg="blue",font=("Arial",35)).place(x=500,y=150)

#frame concept
#white sheet -> container
container = tk.Frame(main,bg="pink")
#pages -> (all pages include inside container)
#register
rg = tk.Frame(container,bg="lightblue")
#login
lg = tk.Frame(container,bg="lightgreen")
#dashboard
dg = tk.Frame(container,bg="orange")

s25 = tk.Frame(container,bg="gray")

for page in (container, rg, lg, dg, s25):
    page.place(x=0,y=0,width=1920,height=1080)

#Register Page
#title
tk.Label(rg,text="Register Form",bg="lightblue",fg="white",font=("Arial bold",35)).place(x=600,y=150)
#user Name
tk.Label(rg,text="User Name :",bg="lightblue",fg="white",font=("Arial",25)).place(x=500,y=250)
rg_name = tk.Entry(rg,bg="lightblue",fg="white",font=("Arial",25))
rg_name.place(x=700,y=250)
#User Phone
tk.Label(rg,text="User Phone :",bg="lightblue",fg="white",font=("Arial",25)).place(x=500,y=330)
rg_phone = tk.Entry(rg,bg="lightblue",fg="white",font=("Arial",25))
rg_phone.place(x=700,y=330)
#User Email
tk.Label(rg,text="User Email :",bg="lightblue",fg="white",font=("Arial",25)).place(x=500,y=410)
rg_email = tk.Entry(rg,bg="lightblue",fg="white",font=("Arial",25))
rg_email.place(x=700,y=410)
#Password
tk.Label(rg,text="Password :",bg="lightblue",fg="white",font=("Arial",25)).place(x=500,y=490)
rg_pass = tk.Entry(rg,bg="lightblue",fg="white",font=("Arial",25),show="*")
rg_pass.place(x=700,y=490)
#login Page button
tk.Button(rg,text="Login Form",bg="gray",fg="white",font=("Arial bold",25),command=lambda:sp(lg)).place(x=550,y=600)
#Register Data button
tk.Button(rg,text="Register",bg="gray",fg="white",font=("Arial bold",25),command=register).place(x=800,y=600)

#Login page
tk.Label(lg,text="Login Form",bg="lightgreen",fg="white",font=("Arial bold",35)).place(x=600,y=150)
#login Email
tk.Label(lg,text="User Email :",bg="lightgreen",fg="white",font=("Arial",25)).place(x=500,y=250)
lg_email = tk.Entry(lg,bg="lightgreen",fg="white",font=("Arial",25))
lg_email.place(x=700,y=250)
#Password
tk.Label(lg,text="Password :",bg="lightgreen",fg="white",font=("Arial",25)).place(x=500,y=330)
lg_pass = tk.Entry(lg,bg="lightgreen",fg="white",font=("Arial",25),show="*")
lg_pass.place(x=700,y=330)
#login Page button
tk.Button(lg,text="Register Form",bg="gray",fg="white",font=("Arial bold",25),command=lambda:sp(rg)).place(x=550,y=450)
#Login Data button
tk.Button(lg,text="Login",bg="gray",fg="white",font=("Arial bold",25),command=login).place(x=850,y=450)


#Login Form
tk.Label(dg,text="Welcome to Amazon",bg="orange",fg="white",font=("Arial bold",35)).place(x=600,y=150)

img = Image.open(r"C:\Users\prave\Downloads\amazon_PNG5.png")
img = img.resize((100,100))
pic = ImageTk.PhotoImage(img)
tk.Label(dg,image=pic,background="orange").place(x=150,y=150)

img1 = Image.open(r"C:\Users\prave\OneDrive\Pictures\sm25.jpg")
img1 = img1.resize((200,200))
sam25 = ImageTk.PhotoImage(img1)
tk.Button(dg,image=sam25,command=lambda : sp(s25)).place(x=350,y=350)


ttk.Combobox(dg,values=["Salem","Chennai","Kovai"]).place(x=450,y=250)


tk.Text(dg,font=("Arial",20),width=15,height=6).place(x=600,y=350)



rg.tkraise()
main.mainloop()

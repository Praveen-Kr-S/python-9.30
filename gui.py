# tkinter

import tkinter as tk

def sp(pg):
    pg.tkraise()



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

for page in (container, rg, lg, dg):
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
tk.Button(rg,text="Register",bg="gray",fg="white",font=("Arial bold",25)).place(x=800,y=600)

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
#Register Data button
tk.Button(lg,text="Login",bg="gray",fg="white",font=("Arial bold",25),command=lambda:dg.tkraise()).place(x=850,y=450)




lg.tkraise()
main.mainloop()

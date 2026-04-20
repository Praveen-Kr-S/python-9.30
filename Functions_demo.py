#Functions
#User Defined Functions
#1.Without Argument Function
def fire():
    print("Fire Mode Is On.......")
# fire()
# print("Hello")
# print("Hello guys..")
# fire()
# fire()
#2.With Argument Function
# Positional Argument functions
def add(x,y):
    a=x
    b=y
    c=a+b
    print("Add :",c)

# add(30,60)
# add(20,25)

#default arguments functions
def full_name(fn="Naveen",ln="Kumar"):
    print(fn+" "+ln)
# full_name()
# full_name("Suresh")
# full_name("Mohan","Raj")

#keyword argument functions
"""
def function_name(**variable):
    #Block of code..
    
function_name(key=value,key=value)
"""
def info(**d):
    print(d)
    print(type(d))
    for i,j in d.items():
        print(i,":",j)

# info(Brand="Samsung",Model="S25",Price=80000,Color="Black")

#variable argument functions
"""
def function_name(*variable):
    #Block of code..

function_name(no of arguments..)
"""

def students(*n):
    print(n)
    print(type(n))
    for i in n:
        print(i)
students("Naveen","Mohan","Naga Raj","Pradeepa","Aarathi")


























#3.Return t5ype functions
"""
it is two types
1.return type without argument function
2.return type with argument function


syntax :

def functionname(arg/pra):
    #block of code
    return value
"""

# 1.return type without argument function

def mul():
    a = 10
    b = 20
    c = 10*20
    return c

# print(mul())
# d = mul()
# print(d)


# 2.return type with argument function

def shop(url):
    if url == "/":
        return "Home page"
    elif url == "/about":
        return "About page"
    elif url == "/contact":
        return "Contact page"
    else:
        return "PageNot Fount"

# v = shop("/contact")
# print("Web page :",v)

# lambda function
#variable = lambda arguments:single expression
div = lambda x,y : x/y
# print(div(20,4))

dd = lambda : "Naveen"
# print(dd())


# recusrive function

# print("Register Form")
# name = input("Enter your name:")
# email = input("Enter your email:").lower()
# password = input("Enter your password:")

def login():
    print("Login Form")
    lg_name = input("Enter your User Name:")
    if lg_name == name:
        pas = input("Enter your Password:")
        if pas == password:
            print("Login Successful")
        else:
            print("Wrong Password")
            login()
    else:
        print("Invalid Username")
        login()

# login()

#2 factorial

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)

# print("Factorial :",fact(5))
"""
fact(5) -> return 5*fact(4) -> 5*
fact(4) -> return 4*fact(3) -> 5*4* ->20*
fact(3) -> return 3*fact(2) -> 20*3* ->60*
fact(2) -> return 2*fact(1) -> 60*2* ->120*
fact(1) -> 120*1 => 120...
"""

#scope of the function

a1 = 10
def demo():
    global a2,a3
    print(a1)
    a2 = 15
    a3 = "Praveen"
# demo()
# print(a2)
# print(a3)

























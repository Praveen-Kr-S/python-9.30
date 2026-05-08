#syntax of class and object
"""
class class_name:
    #set of attributes and functions


variable = class_name()
"""
from pyexpat import model


class mobile:
    # set of attributes
    brand = None
    model = None
    color = None
    price = None
    #function
    def button(self):
        print(self.brand,"Button help's to mobile on/off..")
        print("END".center(30,"*"))

# m1 = mobile()
# m1.brand = "Samsung"
# m1.model = "S26"
# m1.color = "black"
# m1.price = 80000
# print("Mobile Brand:", m1.brand)
# print("Mobile Model:", m1.model)
# print("Mobile Color:", m1.color)
# print("Mobile Price:", m1.price)
# m1.button()
#
#
# m2 = mobile()
# m2.brand = "Apple"
# m2.model = "17 Pro"
# m2.color = "blue"
# m2.price = 90000
# print("Mobile Brand:", m2.brand)
# print("Mobile Model:", m2.model)
# print("Mobile Color:", m2.color)
# print("Mobile Price:", m2.price)
# m2.button()



# constructor function

"""
class class_name:
    def __init__(self):
        //block of code
"""


class Car:
    brand = None
    model = None
    color = None
    price = None
    def __init__(self,b,m,c,p):
        self.brand = b
        self.model = m
        self.color = c
        self.price = p

        print("Car Brand : ",self.brand)
        print("Car Model : ",self.model)
        print("Car Color : ",self.color)
        print("Car Price : ",self.price)
        print("END".center(30,"*"))


c1 = Car("TATA","PUNCH","MATTE GRAY",800000)
c2 = Car("Hyndai","Creta","Black",1600000)




#Inheritance
#single level inheritance

# class Book_info:#super class
#     name = "Learn Python"
#     def fun1(self):
#         print(f"Book Name : {self.name}")
#
# class Author(Book_info):#sub-class
#     au_name = "Naveen"
#     def fun2(self):
#         print(f"Author Name : {self.au_name}")

# a = Author()
# print(a.au_name)
# print(a.name)
# a.fun2()
# a.fun1()



#Multilevel Inheritance

class Book_info:#super class
    name = "Learn Python"
    def fun1(self):
        print(f"Book Name : {self.name}")

class Author(Book_info):#sub-class
    au_name = "Naveen"
    def fun2(self):
        print(f"Author Name : {self.au_name}")


class Book_price(Author):
    def fun3(self):
        print("Book Price Rs : 700")

class Book_genre(Book_price):
    def fun4(self):
        print("Book Genre : Tech Learning")

# g = Book_genre()
# g.fun4()
# g.fun3()
# g.fun2()
# g.fun1()



#Hierachical Inheritance

class upi:
    def UPI_money_transfer(self):
        print("UPI Money Transfer System")

class gpay(upi):
    def gpay_access(self):
        print("Gpay User Account Access..")

class phonepy(upi):
    def phonepy_access(self):
        print("phonepy User Account Access..")

class pytem(upi):
    def pytem_access(self):
        print("pytem User Account Access..")

# pt = pytem()
# pt.pytem_access()
# pt.UPI_money_transfer()
#
# gp = gpay()
# gp.gpay_access()
# gp.UPI_money_transfer()



#Multiple Inheritance
class Camera:
    def camera_access(self):
        print("Camera Take Good Pictures..")

class Radio:
    def radio_access(self):
        print("Play the Good Songs..")

class Tv:
    def tv_access(self):
        print("Watch the Good Movies..")


class smartphone(Camera,Radio,Tv):
    def smartphone_access(self):
        print("Enjoy the with friends via calling and internet..")

# sm = smartphone()
# sm.smartphone_access()
# sm.tv_access()
# sm.radio_access()
# sm.camera_access()



#Polymorphism

#method overloading/complie time polymorphism
class cal:
    #default argument function
    def add(self,a=None,b=None,c=None,d=None,e=None):
        if a!=None and b!=None and c!=None and d!=None:
            print("4 Arguments Add Value :",a+b+c+d)
        elif a!=None and b!=None and c!=None:
            print("3 Arguments Add Value :",a+b+c)
        elif a!=None and b!=None:
            print("2 Arguments Add Value :",a+b)
        else:
            print("1 Arguments Value :",a)

# c = cal()
# c.add(1,2,3,4)
# c.add(1,2,3)
# c.add(1,2)
# c.add(1)




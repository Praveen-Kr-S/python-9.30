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








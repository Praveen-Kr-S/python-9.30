'''
a = 30 #integer
print(a)
print(type(a))
print(id(a))
a = "Python" #string
print(a)
print(type(a))
print(id(a))
'''
#variables
'''
name = 'Naveen M'
AGE = 20 #integer
City = "Salem" #string
max_mark = 55.8 #float
s2ub1 = False #boolean->True/False


print(name,type(name))
print(AGE,type(AGE))
print(City,type(City))
print(max_mark,type(max_mark))
print(s2ub1,type(s2ub1))


#keywords
#help("keywords")


#operators
a = 5
b = 2
print(a+b)
print(a-b)
c = a*b
print(c)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
print(a**3)

#find the avg 3 number
a=20
b=40
c=30
total=a+b+c
print(total/3)
'''

#find area of triangle
"""
br = 40
h =60
area_of_triangle = (1/2)*b*h

print("area of triangle :",area_of_triangle)
"""


#inputs
#1.compile time input
name = "Praveen"
#2.Run time or user input
"""
synatx of run time input
vaiable = input("input label content")

#Type casting
int(),float(),bool(),complex(),str()
"""
'''
Name = input("Enter Name :")
print(Name,type(Name))

age = int(input("Enter your Age :"))
print(age,type(age))


f = float(input("Enter float data :"))
print(f,type(f))

c = complex(input("Enter data :"))
print(c,type(c))

b = bool(input("Enter data :"))
print(b,type(b))

b = str(55)
print(b,type(b))
'''

#Assignment operator
'''
a = 10
print(a) #10
a+=20
print(a) #30
a -= 15
print(a)
a *= int(input("enter a value :"))
print(a)
a /= 5
print(a)
a %= 2
print(a)
b = int(input("enter b value :"))
b //= 2
print(b)
b **= 2
print(b)
'''


#comparision operator
# ==, !=, >, <, >=, <=
'''
a = 10
b = 20
c = 30
d = 20
print(a == b) #False
print(b == d)
print(a != c)
print(b != d)
print("praveen" != "praveen s")
print(b < c) # 20<30
print(c < a) #30<10
print(c > a)
print(b > d)
print(b >= d)
print(a >= d)
print(a <= d)
print(c <= d)
'''
#logical operator
#and,or,not()
a = 10
b = 20
c = 10

print(a != b and b >= a) #True
print(a != b and b >= a and c > a)

print(a == b or b <= a or c >= a)

print(not(a != c and b >= a))




















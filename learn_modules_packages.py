#Modules
"""
modules -> collection of variables, functions and classes
basic -> math,calendar,randon,time,datetime
advanced  -> pywhatkit,webbrowser
packages -> collection of modules and sub_packages
pygame,pillow(PIL),numpy,pandas,scipy,matplotlib

libraies -> collection of packages -> flask
frameworks -> collection of library -> djando,fast_api
"""
#build_in_modules
# 1 Math
import math
# f = math.factorial(5)
# print("Factorial : ",f)
# print(math.pi)
# print(math.pow(5,3))
# print(math.floor(4.9))
# print(math.ceil(4.1))
# print(math.remainder(5,2))

#2.calendar
import calendar as cd
# print(cd.calendar(2026))
# print(cd.month(2026,4))
# print(cd.isleap(2026))
# print(cd.isleap(2024))
# print(cd.SUNDAY)
# print(cd.MONDAY)

#3.datetime
import datetime as dt
# ct = dt.datetime.now()
# print(ct)
# print(ct.date())
# print(ct.time())
# print(ct.day)
# print(ct.month)
# print(ct.year)
# print(ct.hour)
# print(ct.minute)
# print(ct.second)
# print(ct.microsecond)
#
# cs = dt.datetime(2027,1,1,12,24,35)
# print(cs)
# print(cs.date())
# print(cs.year)
# print(cs.date()-ct.date())


import random as rd
# print(rd.random())
# print(rd.randint(10000,20000))
# print(rd.randrange(1000,2000,100))
# l = [200,"Praveen","Mohan",True,"Naveen"]
# print(rd.choice(l))
# print(rd.choices(l,k=3))

#time
import time as t
# print(t.ctime())
# print("Hello Pradeepa..")
# t.sleep(2)
# print("Hello Naveen..")
# print(t.strftime("%d/%m/%Y %H:%M:%S"))

#pywhatkit
import pywhatkit as pk
# pk.search("TVK")
# pk.playonyt("vj siddhu vlog")
# pk.sendwhatmsg_instantly("+91 8940296171","Hello Mohan Rajj😊")


import webbrowser as wb

# wb.open("https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true")
# wb.open_new_tab("https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true")

















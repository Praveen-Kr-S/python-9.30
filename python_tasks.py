#compound intrest
"""
A = P*(1+(r/n))**(n*t)
"""
"""
P = int(input("Priciple Amount :"))
r = float(input("Rate of Intrest :"))
n = int(input("No of time intrest increase :"))
t = int(input("Total Years :"))
A = P*(1+(r/n))**(n*t)
print("compound intrest amount :",A)
"""

#swapping two values using temp variable
'''
a = 10
b = 5
print("Before Swapping a :",a)
print("Before Swapping b :",b)
t = a #10
a = b #5
b = t #10
print("After Swapping a :",a)
print("After Swapping b :",b)
'''
#swapping two values using without temp variable
'''
a = 10
b = 5
print("Before Swapping a :",a)
print("Before Swapping b :",b)
a = a+b #15
b = a-b #15-5=10
a = a-b #15-10=5
print("After Swapping a :",a)
print("After Swapping b :",b)
'''
#find suquare root of number
'''
v = int(input("Enter Number :"))
sq = v**0.5
print("suquare root value :",sq)
'''
#find last number in digits
'''
n = int(input("Enter Number :"))
#12345%10 ->1234.5->5
ln = n%10
print("last number :",ln)
'''

#Bitwise operator
"""
step-1
decimal  0-9 => 10 -> binary code 2
step-2
binary code -> decimal
"""
"""
gb,mb,kb,byte, 8bit = 1byte

      128   64   32   16   8   4   2   1  -> total 255     
       0    1    0     0   0   0   0   1  ->65 ->x
       0    1    0     1   1   0   0   0  ->88 ->y
AND &  0    1    0     0   0   0   0   0  ->64 decimal 
OR  |  0    1    0     1   1   0   0   1  ->89 decimal
XOR ^  0    0    0     1   1   0   0   1  ->25 decimal

bitwise compliment (~)
-(n+1)
n - decimal no
-(-4+1) => -5
"""
x=65
y=88
print(x&y)
print(x|y)
print(x^y)
print(~4)
print(~-4)


































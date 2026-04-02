#loops-Hollow patterns
"""
print("i - Vales")
n=5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
    
print("j - Vales")
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()


print("----------------")
#hollow square:
for i in range(n):
    for j in range(n):
        if i==0 or i == 4 or j==0 or j==4:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()    

#Plus Pattern
print("----------------")
for i in range(n):
    for j in range(n):
        if i==2 or j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#Cross Pattern
print("----------------")
for i in range(n):
    for j in range(n):
        if i==j or i+j == 4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#Hollow square + Assci Pattern
print("----------------")
'''
c=90
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==4 or j==4:
            print("*",end=" ")
        else:
            print(chr(c),end=" ")
            c=c-1
    print()

'''

#Cross Pattern with alphabet
print("----------------")
s = "APPLE"
#string indexing
#print(s[0])
for i in range(n):
    for j in range(n):
        if i==j or i+j == 4:
            print(s[i],end=" ")
        else:
            print(" ",end=" ")
    print()

#half hollow pramid
print("----------------")
for i in range(n):
    for j in range(n):
        if i==4 or j == 0 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""

#while loop
"""
1.inc
2.dec
3.infinity

Syntax while loop
step - 1
varible =value
        step-2
while condition:
        step-3
    #looping statement
    step-4
    #inc/dec
"""

#while - inc
'''
i=5
while i<=10:#False
    print(i)
    i+=1
'''
#while - dec
"""
i=5
while i>=1:#True
    print(i)
    i-=1
"""
#while - infinity
#1-condition
'''
i=5
while True:
    print(i)
    i+=1
'''
#2-INC/DEC
"""
i=5
while i<=10:
    print(i)
    i-=1
"""


#Fibonacci series:
"""
default = 0,1

0+1=1+1=2=3=5=8=13=21
"""
'''
n1=0
n2=1
for i in range(10):
    #    3 + 5
    n3 = n1+n2
    print(n3)#12358
    n1=n2
    n2=n3
'''





















    




































    

    

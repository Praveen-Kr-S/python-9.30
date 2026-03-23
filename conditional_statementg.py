#conditional statement/selection control

"""
1.Syntax of if statement

if condition:       --> True (conditional.logical,special operator)
    #True statement

"""
#1
'''
b = int(input("Enter the value :"))
if b==0: #False
    print(b,"is zero!")
'''

"""
2.Syntax of if-else statement

if condition:       --> True (conditional,logical,special operator)
    #True statement
else:
    #False Statement
"""

#2
'''
m = int(input("Enter M Value :"))
n = int(input("Enter N Value :"))
if m>n:#false
    print("Quation :",m//n)
    print("Remainder :",m%n)
else:
    print("N is greaterthan M..")
    
#3. find odd or even number
    
b = int(input("Enter the value :"))
if (b%2) == 0: 
    print(b,"is even number..")
else:
    print(b,"is not a even number..")
'''

#4.find the vowels sound
'''
c = str(input("Enter the Letter (A to Z) :"))
if c=="A" or c=="E" or c=="I" or c=="O" or c=="U":
    print(c,"is Vowel Sound..")
else:
    print(c,"is not a Vowel Sound..")
'''

"""
2.Syntax of if-elif-else statement

if condition:       --> True (conditional,logical,special operator)
    #True statement
elif condition:
    #True statement
elif condition:
    #True statement
else:
    #False Statement
"""

#5.Find the grade of students based on average

"""
100-90 ->A+
89-80 ->A
79-70 ->B+
69-60 ->B
avg<60 -> Fail
"""
'''
avg = 65
if avg<=100 and avg>=90:
    print("A+ Grade")
elif avg<90 and avg>=80:
    print("A Grade")
elif avg<80 and avg>=70:
    print("B+ Grade")
elif avg<70 and avg>=60:
    print("B Grade")
else:
    print("Student is Fail..")
'''


#Nested if
"""
2.Syntax of Nested statement
if condition:     
    if condition:     
        if condition:     
            #True statement
        else:
            #False Statement
    else:
        #False Statement
else:
    #False Statement
"""

email = input("Enter Email Id :")
if email == "abc@gmail.com":
    pas = int(input("Enter Password :"))
    if pas == 1234:
        print("Login Sucess!")
    else:
        print("Worng Password")
else:
    print("Invaild Email Id")











































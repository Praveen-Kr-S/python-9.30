#Strings
"""
* Srting is immutable datatype
* String is sequence of character

"hello@$1234 ^7" or ''

#String Indexing
Backward indexing <-   -6 -5 -4 -3 -2 -1 
                  a =  "P  Y  T  H  O  N"
Forward indexing  ->ckward indexin    0  1  2  3  4  5 

"String_data"[Index_Value] or variable[Index_Value]

"""
#String Indexing
"""
a = "Mohan Raj"
print(a)
print(a[2])
print(a[6])
print(a[-1])
print(a[-5])
#reverse string
print(a[::-1])
print(a[::-2])

#String Silicing
s= "hello i am pradeepa, full stack developer in hCL"
#variabe[start:end(n-1)]

print(s[8:10])
print(s[11:19])
print(s[11:])
print(s[:-1])

print(type(str(4646)))
print(len(s))
#Build in functions in strings
'''
"String_data".build_in_function or variable.build_in_function
'''
print("Hello".upper())
b="PK@gmail.com"
print(b.lower())
print(s.title())
print(s.capitalize())
print("HELLO PRAVEEN".casefold())
print("Hello BhraTHI".swapcase())
print("m.naveen".center(30))
print("m.naveen".center(30,"*"))
print("Hello World!".count("l"))
print(b.index('m'))
print("Praveen Kumar".rindex('a'))
print("Hello hey bye hi ".index('e',3))
"""

#String task
#1.Remove duplicate
'''
s = "Hello World!"
c = ""
for i in s[::-1]:
    if i not in c:
        c+=i

print(c)
'''       
    
#count the vowles in string
'''
n = "Praveen"
c=0
v="aeiouAEIOU"
for i in n:
    if i in v:
        c+=1

print("Count of vowles :",c)
'''

#String functions

s1 = "Hello Naveen"
print(s1.find('e'))
print(s1.find('z'))
print(s1.rfind('e'))
s2 = s1.replace('H','h')
print(s2)
print("Hello world".endswith('lD'))
print("Hello world".startswith("Ho"))
#1
c="Hello {}, I am {}"
print(c.format("Mohan","Naveen"))
print(c)
#2
a,b="Praveen","Nagaraj"
print(f"Name : {a}")

print("     Praveen                      ")
print("     Praveen                      ".strip())
n="hello i am pradeepa full stack developer in hCL"
n1 = n.split()
print(n1)#list
j = ' '.join(n1)
print(j)

#encode and decode
n="hello i am Mohan full stack developer in hCL"
print(n)
e = n.encode('UTF-32')
print(e)
d = e.decode('UTF-32')
print(d)

#escape sequence ->\n-newline,\t ->new tab
print("hello\ni am Mohan\nI am full stack developer in\thCL")

print("Naveen is\nCM in\n2026".splitlines())


#build in functions for validation

print('praveen'.islower())
print("KUMAR".isupper())
print("Praveen".istitle())
print("Praveen1".isalpha())
print("23241".isdigit())
print("23241fgrr".isalnum())
print("a b".isidentifier())
print("Hello #$^^#!~,.ghdfhg      வணக்கம்uys".isascii())


#remove e in specific string
b = """
s = "Praveen"
v=''
for i in s:
    if i not in 'e':
        v+=i

print(v)

#to get the specific value in string -e
s = "Praveen"
v=""
for i in s:
    if i == 'e':
        v+=i

print(v)

"""
print(b)


#syntax of try- except
"""
try:
    #block of code
except Exception as e
    #Show the exception
"""
'''
try:
    #name error
    b = 10
    print(b1)
except Exception as e:
    print(e)
'''
'''
try:
    #ZeroDivisionError
    a = 10
    b = 0
    print(a/b)
except Exception as e:
    print("0 No divisable")


try:
    #list index out of range
    a = [10,20,30,40]
    print(a[2])
except Exception as e:
    print(e)
finally:
    print("Program Finished")
'''

#assert
#assert condition
'''
a = 101
assert a == 10
print(a)
'''


#raise

try:
    a = 10
    b = 0
    c = 3

    if b == 0:
        raise ZeroDivisionError("Zero is not divisable")

    print(a+b+c)
    print(a/b)
except Exception as e:
    print(e)


























    

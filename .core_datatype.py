#core data type
a = 10
print(a)
a = "Praveen"
print(a)

#List
a = [10,"Praveen","Praveen",80,['hello',True],False,44.87]
print(a)
print(a[3])
print(a[-1])
#print(a[7])
print(a[2:6])
print(a[::-1])
print(a[4][-2])

#Build in functions in list:
#variable.build-in-functions

print(a.index(False))
print(a.count("Praveen"))

#add
print(a)
a.append("Django")
print(a)
a.insert(3,'React.js')
print(a)
l=[67,89.4,"bye"]
a.extend(l)
print(a)

#remove
a.remove(80)
print(a)
a.pop()
print(a)
a.pop(1)
print(a)
#a.clear()
#print(a)


b = a.copy()
print("b :",b)

a.reverse()
print(a)

l = [78,22,45,95,5,2,56,38]
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)


"""
for i in l:
    print(i)
"""

#1.remove duplicate element in list
"""
l1 = [67,55,67,89,55,"Bye"]
ans = []
for i in l1:
    if i not in ans:
        ans.append(i)
print(l1)
print(ans)
"""
#2.find max no in list

l = [34,56,78,23,98,67]
v = 0
c = l[0]#34
for i in l:
    if i<c:
        v=i

print(v)






        
    


































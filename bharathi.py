#Core data types
#tuple
# t = (20,30,56.7,"Python",True,("Hello",7+8j),30)
# print(t)
# print(type(t))
#
# print(t[4])
# print(t[5][1])
# print(t[2:5])
#
# # build - in - functions
# print(t.count(31))
# print(t.index(True))
#
# # convert tuple to list
# l = list(t)
# print(l,type(l))
# l.pop(2)
# t = tuple(l)
# print(t,type(t))
#
# a = (56,)
# print(a,type(a))
#
# b = 20,40,True,"Hello"
# print(b,type(b))


#Set ->{}
# s = {20,30,55.76,30,20,30,"Praveen",False}
# print(s)
# print(type(s))
#
# #build-functions in set
# # add
# s.add("java")
# print(s)
# t = (4000,5000,6000,5000)
# s.update(t)
# print(s)
# # remove
# s.remove(4000)
# print(s)
# s.discard(30)
# print(s)
# s.pop()
# print(s)
# # s.clear()
# # print(s)
# s1 = s.copy()
# print(s1)
#
# # veen method
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
#
# print("Intersection :",a.intersection(b))
# print("a :",a)
# # a.intersection_update(b)
# # print("a :",a)
#
# print("symmetric_difference :",a.symmetric_difference(b))
# print("a :",a)
# # a.symmetric_difference_update(b)
# # print("a :",a)
#
#
# print("difference of a :",a.difference(b))
# print("a :",a)
# # a.difference_update(b)
# print("a :",a)
# print(a.union(b))
#
#
# x = {1,2,3,4,5,6,7}
# y = {1,2,3,4,5}
# z = {10,20,30,40,50}
# print(x.issubset(y))
# print(y.issubset(x))
# print(x.issuperset(y))
# print(y.isdisjoint(z))


# dictionary
# variable = {key:value,key:value}
data = {"name":"Praveen",
        "age":25,
        "course":"django",
        "city":"Salem",
        "name1":"Praveen"
        }

print(data)
print(type(data))

# print(data["name"])
# print(data["age"])
# print(data["course"])

# build-in-functions in dictionary
# print(data.keys())
# print(data.values())
# print(data.items())

for i in data.items():
    print(i)

for i,j in data.items():
    print(i," : ",j)
print("******************")
for i in data:
    print(i," : ",data[i])


stds = {
    "std1":{"name":"Pradeepa","course":"AI","id":21},
    "std2":{"name":"Aarthi","course":"Python","id":22},
    "std3":{"name":"Mohan","course":"Django","id":23},
    "std4":{"name":"Naga raj","course":"react.js","id":24}
}

# print(stds)
# print(stds.get("std1"))
# print(stds["std2"])


# for i in stds["std3"]:
#     print(i," : ",stds["std3"][i])


for i,j in stds.items():
    print(i)
    for k,v in j.items():
        print(k," : ",v)















































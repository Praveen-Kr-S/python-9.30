#Single level thread
import threading as t
'''
def ebook(n):
    print("Book Name : ",n)


#ebook("Learn Java")
t1 = t.Thread(target = ebook, args = ("Learn Python",))
t1.start()
'''


#Multi-line thread

def ebook(n):
    print("Book Name : ",n)


def author(n):
    print("Author Name : ",n)


#ebook("Learn Python")
#author("Surjit")


t1 = t.Thread(target=ebook,args=("Learn Python",))
t2 = t.Thread(target=author,args=("Surjith",))
#t1.start()
#t1.join()
#t2.start()




#Daemon Thread
def ebook(n):
    print("Book Name : ",n)

t1 = t.Thread(target=ebook,args=("Learn Python",))
t1.setDaemon(True)
print(t1.isDaemon())
t1.start()






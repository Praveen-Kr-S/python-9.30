import socket

s = socket.socket()

host = socket.gethostname()
print(host)
port = 7788

s.connect((host,port))

msg = s.recv(1024)
print(msg)
s.send(b"Message recived sucessfully")
s.close()


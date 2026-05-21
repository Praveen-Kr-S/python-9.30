import socket

s = socket.socket()

host = socket.gethostname()
print(host)
port = 7788
s.bind((host,port))
s.listen(3)
while True:
    conn, addr = s.accept()
    print(addr)
    conn.send(b"Hello mohanraj, I am server")
    print(conn.recv(1024))
    conn.close()


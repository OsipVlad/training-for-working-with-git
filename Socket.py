import socket

sock = socket.socket()
sock.bind(("", 9090))
sock.listen(1)

print("---Start listen port 9090---")

conn, addr = sock.accept()
print(addr)


import socket

sock = socket.socket()
sock.connect(("localhost", 9090))
messages = "hello, world"

sock.send(messages.encode("utf-8"))

import socket

sock = socket.socket()
sock.connect(("localhost", 9090))
messages = input("Vvod dannih: ")

sock.send(messages.encode("utf-8"))

import socket
from time import sleep

sock = socket.socket()
sock.bind(("", 9090))
sock.listen(1)

print("---Start listen port 9090---")

while True:
    conn, addr = sock.accept()
    print(addr)


    server_working = True
    current_data_all = ''
    while server_working:

        current_data = conn.recv(1)
        sleep(0.3)

        current_data_all += current_data.decode("utf-8")


        if not current_data:
            server_working = False
        print(current_data)
    print(current_data_all)

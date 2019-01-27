import socket
import time

def server():
    print("Start")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 1234))
    server.listen(1)
    (connection, adress) = server.accept()
    while (connection, adress):
        data = connection.recv(100).decode("UTF-8")
        print(data)
        connection.send("12345678901234567890123456789009".encode("UTF-8"))
        data = connection.recv(300).decode("UTF-8")
        print(data)
        connection.send("11111111111111111111111111111111".encode("UTF-8"))
        connection.close()
        (connection, adress) = server.accept()
    print("End")

server()
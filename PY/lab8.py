# 1a. Sa se implementeze folosind modulul socket (peste TCP), un server care atunci cand un client se conecteaza, scrie intr-un fisier text : timpul conexiunii (in format human-readable), adresa si portul clientului.

import socket, time

def user_connected():
    print("START")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 1234))
    server.listen(3)
    (connection, address) = server.accept()

    while (connection, address):
        print(connection)
        print(address)

        data = connection.recv(100).decode("UTF-8")
        print(data)
        if data == "exit":
            break

        connected_users_file = open(r"C:\Users\crist\OneDrive\Documents\GitHub\Retele-Neuronale\PY\connected_users.txt", "a")
        curr_time = time.ctime(time.time())
        user_data = "\n" + curr_time + " | " + str(address[0]) + " | " + str(address[1])
        connected_users_file.write(user_data)
        connected_users_file.close()
        connection.close()
        (connection, address) = server.accept()
    print("END")

# user_connected()

# 1b. Sa se implementeze un client pentru serverul implementat la 1a: un script care primeste de la linia de comanda un string addr si un integer port si se conecteaza prin TCP la adresa addr, la portul port.

import socket, sys

def client():
    if len(sys.argv) >= 2:
        addr = sys.argv[1]
        port = int(sys.argv[2])

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((addr, port))
        server.send(b"exit")
        server.close()

# client()

# 2a. Sa se implementeze folosind modulul socket (peste UDP), un server care atunci cand primeste un pachet UDP (datagrama), scrie intr-un fisier text urmatoarele informatii: ora si data, adresa, port, lungime, hash-ul md5 pe continut in format hex, hash-ul sha256 pe continut in format hex.


# 2b. Sa se implementeze un client pentru serverul implementat la 2a: un script care primeste de la linia de comanda un string addr, un integer port, si un string msg si trimite un pachet UDP la adresa addr, la portul port si cu continutul msg.

# 3. Sa se porneasca un server care sa expuna fisierele si directoarele din directorul curent. Accesati acel server dintr-un browser, si apoi folosind un client HTTP in python (urllib.request)

# 4. Odata pornint server-ul de la punctul 3, sa se extraga numele fisierelor .txt si sa se afiseze in consola.

# 5. Sa se scrie un script, care primeste de la linia de comanda (ca argument) un URL, si descarca in directorul curent toate imaginile (img src). 

# 6. Sa se scrie un script care primeste de la linia de comanda (ca argument) un URL si scrie intr-un fisier urmatoarele informatii: status-ul raspunsului, marimea raspunsului, tipul raspunsului (daca este cunoscut), hash-uri md5 pentru fiecare fragment de maxim 1000 bytes din raspuns si timpul de raspuns al server-ului.
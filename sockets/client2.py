import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connected to server.")

client.connect(("localhost", 5002))
name = None

def menu():
    print("Welcome!\n")
    action = input("1 to registrate, 2 to autorize: ")

    if action == "1":
        username = input("Enter your name: ")
        login = input("Enter your login: ")
        password = input("Enter your password: ")

        client.send("1".encode())
        client.send(f"{username}.{login}.{password}".encode())

        response = client.recv(1024).decode()
        if response == "1":
            return menu()
        if response == "2":
            print("Error. Such login is already exist.")
            return menu()

    elif action == "2":
        login = input("Enter your login: ")
        password = input("Enter your password: ")

        client.send("2".encode())
        client.send(f"{login}.{password}".encode())

        response = client.recv(1024).decode()
        if response == "2":
            print("Error. Check your login and password.")
            return menu()
        else:
            global name
            name = response
            thread = Thread(target=recv_message, daemon=True)
            thread.start()
    else:
        print("No such action was found.")
        return menu()

def recv_message():
    print("Koroche poluchaem soobshenie.")
    while True:
        message = client.recv(1024).decode()
        print("\n" + message)

menu()

while True:
    msg = input("Enter your message: ")
    if msg == "quit":
        break

    client.send((name + ": " + msg).encode())

client.close()
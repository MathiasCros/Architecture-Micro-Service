import socket

# Création d'une socket côté client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.16.20.104", 63000))

while True:
    alire = input(">")
    client.send(alire.encode())

    msg = client.recv(1024).decode()
    if msg == "fin":
        break
    print(f"Retour : {msg}")

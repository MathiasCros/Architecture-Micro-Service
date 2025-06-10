import socket
#Création d'une socket côté serveur

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#172.16.20.104
serveur.bind(("172.16.20.104", 63000))
serveur.listen(1)

conn, addr = serveur.accept()

while True:
    msg = conn.recv(1024).decode()
    if msg == "fin":
        break   
    conn.send(msg.encode())
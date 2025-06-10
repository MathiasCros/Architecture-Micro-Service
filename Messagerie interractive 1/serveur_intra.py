import socket
#Création d'une socket côté serveur

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#172.16.20.104
serveur.bind(("172.16.20.104", 63000))
serveur.listen(1)

conn, addr = serveur.accept()

# Côté serveur
while True:
    message = conn.recv(1024).decode()
    print("Client dit:", message)
    if (message == "fin"):
        break
    reponse = input("Répondre > ")
    conn.send(reponse.encode())
    if (reponse == "fin"):
        break

import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.send("Bonjour serveur !".encode())

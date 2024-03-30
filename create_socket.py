import socket

# Création d'un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
server_address = ('localhost', 12345)
sock.connect(server_address)

# Envoi de données
message = 'Hello, world!'
sock.sendall(message.encode())

# Réception de données
response = sock.recv(1024)
print(response.decode())

# Fermeture du socket
sock.close()
 
import socket
import select

host = ''
port = 4242

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((host, port))
connection.listen(5)
print(f"Serveur listening on port {port}")

clients = []
while True:

    connections_waiting, wlist, xlist = select.select([connection],[], [], 0.05)
    
    for con in connections_waiting:
        connection_with_clients, infos = connection.accept()
        # On ajoute le socket connecté à la liste des clients
        clients.append(connection_with_clients)
    
    clients_to_read = []
    try:
        clients_to_read, wlist, xlist = select.select(clients, [], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in clients_to_read:
            # Client est de type socket
            msg_rcv = client.recv(1024)
            # Peut planter si le message contient des caractères spéciaux
            msg_rcv = msg_rcv.decode()
            print("Received {}".format(msg_rcv))
            client.send(b"Received")

print("Close connection")
for client in clients:
    client.close()

connection.close()
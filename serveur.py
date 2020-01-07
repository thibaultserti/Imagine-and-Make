#!/usr/bin/env python3
#-*-coding:utf-8-*-
import socket
import select
import signal
import sys
from lib import *

def signal_handler(sig, frame):
    print("Connexion fermée")
    for client in clients:
        client.close()
    connection.close()
    sys.exit(0)

def book(client):
    client.send("BOOK")


def modify_csv(client):
    pass

host = ''
port = 4242

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((host, port))
connection.listen(5)
print(f"Le serveur écoute sur le port {port}")

clients = []
while True:

    signal.signal(signal.SIGINT, signal_handler)
    #signal.pause()

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
            if msg_rcv.split(" ")[0] == "UNBOOK":
                modify_csv(client)
            if msg_rcv == "END":
                client.close()
                clients.remove(client)

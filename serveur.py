#!/usr/bin/env python3
#-*-coding:utf-8-*-
import socket
import select
import signal
import sys

import socket
import select
import signal
import sys
import sqlite3


def signal_handler(sig, frame):
    print("Connexion fermée")
    for client in clients:
        client.close()
    connection.close()
    sys.exit(0)

def state_bdd(client):
    try:
        sqliteConnection = sqlite3.connect('website/db.sqlite')
        cursor = sqliteConnection.cursor()
        print("Base de donnée connectée !")
        sql_update_query = """SELECT "Réservé" FROM "Chambers" WHERE "Numéro de chambre" = ?"""
        cursor.execute(sql_update_query, client)
        reserved = cursor.fetchone()
        sqliteConnection.commit()
        print("Enregistrement mis à jour")
        cursor.close()
    except sqlite3.Error as error:
        print("Erreur lors de la connexion", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("La connexion à la BDD a été fermée")
            return reserved

def modify_bdd(client):
    try:
        sqliteConnection = sqlite3.connect('website/db.sqlite')
        cursor = sqliteConnection.cursor()
        print("Base de donnée connectée !")
        sql_update_query = """Update "Chambers" SET "Réservé" = "" WHERE "Numéro de chambre" = ?"""
        cursor.execute(sql_update_query, client)
        sqliteConnection.commit()
        print("Enregistrement mis à jour ")
        cursor.close()

    except sqlite3.Error as error:
        print("Erreur lors de la connexion", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("La connexion à la BDD a été fermée")

def book(chamber):
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

    connections_waiting, wlist, xlist = select.select([connection],[], [], 0.05)
    
    for con in connections_waiting:
        connection_with_clients, infos = connection.accept()
        # On ajoute le socket connecté à la liste des clients
        msg_rcv = connection_with_clients.recv(1024)
        chamber = msg_rcv.decode()
        print(chamber)
        clients.append((connection_with_clients,chamber))
    
    c = [e[0] for e in clients] # very ugly
    clients_to_read = []
    try:
        clients_to_read, wlist, xlist = select.select(c, [], [], 0.05)
        clients_to_read = [(c,num[1]) for c,num in zip(clients_to_read, clients)] # very very ugly but works

    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in clients_to_read:
            # Client est de type socket
            msg_rcv = client[0].recv(1024)
            # Peut planter si le message contient des caractères spéciaux
            msg_rcv = msg_rcv.decode()
            print(f"Reçu {msg_rcv}")
            client[0].send(b"Ok")

            if state_bdd(client[1]) == "X":
                book(client[0])

            if msg_rcv == "UNBOOK":
                modify_bdd(client[1])
                print("unbooked")

            if msg_rcv == "END":
                client[0].close()
                clients.remove(client)
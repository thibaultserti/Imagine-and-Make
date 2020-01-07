import socket

host = "localhost"
port = 4242

connection_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_with_server.connect((host, port))
print(f"Connection established with serveur on port {port}")

msg = b""
while msg != b"END":
    msg = input("> ")
    msg = msg.encode()
    connection_with_server.send(msg)
    msg_rcv = connection_with_server.recv(1024)
    print(msg_rcv.decode())

print("Close connection")
connection_with_server.close()
import socket
import sys

HOST='127.0.0.1'
PORT=19000
BUFSIZ=1024
ADDR = (HOST,PORT)

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 19000
serversocket.bind(ADDR)

serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    while 1:
        data = clientsocket.recv(253)
        print(data)

    clientsocket.close()

    print("Connec Add: %s" % str(addr))

    '''msg = 'Welcome!' + "\r\n"
    clientsocket.send(msg)
    clientsocket.close()'''
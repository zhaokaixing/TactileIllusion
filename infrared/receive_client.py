import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 19001

s.connect((host, port))
msg = s.recv(1024)

s.close()

print (msg)
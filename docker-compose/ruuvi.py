from ruuvitag import RuuviTag
import socket
import time
import json
SERVER_IP = "localhost"
PORT = 8094


class Connect(object):
    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((SERVER_IP, PORT))
        return sock

    def send(self, command):
        sock = self.connect()
        sock.sendall(command.encode('utf-8'))
        sock.close()


connect = Connect()

while True:
    for tag in RuuviTag.scan():
        print(tag)
        connect.send(str(tag))

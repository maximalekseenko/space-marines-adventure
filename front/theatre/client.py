import socket
import pickle



class Client:
    def __init__(self, address):
        self.client = socket.socket()
        self.address = address

        self.is_connected = False


    def Connect(self):
        self.client = socket.socket()
        if self.is_connected:
            print("- client: already connected.")
            return True
        try:
            self.client.connect(self.address)
            print("- client: connection success.")
            self.is_connected = True
            return True
        except Exception as e:
            print(e)
            print("- client: connection failed.")
            self.is_connected = False
            return False


    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)


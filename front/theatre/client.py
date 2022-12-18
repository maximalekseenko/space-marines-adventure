import socket
import json
import _thread



class Client:
    def __init__(self, address):
        self.socket:socket.socket
        self.address = address

        self.is_connected = False

        self.game_id = -1


    def Connect(self) -> bool:

        # create socket
        self.socket = socket.socket()

        # check if already connected
        if self.is_connected:
            print("- client: already connected.")
            return True

        # attempt to connect
        try:
            self.socket.connect(self.address)
        # fail
        except:
            print("- client: connection failed.")
            self.is_connected = False
            return False

        # send settings
        self.socket.send(json.dumps({'name':"labyrinth", 'players':"-1"}).encode())

        # get game id
        self.game_id = int(self.socket.recv(1024).decode())

        # log success
        print("- server: connection success.")
        self.is_connected = True

        # create a thread
        _thread.start_new_thread(self.Thread, ())

        return True


    def Send(self, data):
        try:
            self.socket.send(json.dumps(data).encode())
            return data
        except socket.error as e:
            print(e)


    def Thread(self):

        # join
        self.socket.send(json.dumps({'name':"join", 'value':"player"}).encode())

        # log thread creation
        print("- client: thread created.")

        while True:
            try:
                # get data
                data = json.loads(self.socket.recv(4096).decode())
                self.Handle_Request(data)
            except Exception as e: 
                print(f"-connection lost due to:", e)
                break
        self.socket.close()


    def Handle_Request(self, data:dict) -> None:
        print(data)
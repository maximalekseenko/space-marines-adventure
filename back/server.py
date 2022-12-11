import socket
import json
import _thread
from game.game import Game



SERVER_ADDRESS = ("0.0.0.0", 5555)



class Server:
    def __init__(self) -> None:        
        self.socket:socket.socket
        self.games:list[Game] = list()

        
    _game_id = -1
    def Get_Game_ID(self) -> int:
        self._game_id += 1
        return self._game_id

    
    def Init(self):
        # create socket
        self.socket = socket.socket()

        # connect
        self.socket.bind(SERVER_ADDRESS)

        # start listen
        self.socket.listen(2)

        # log
        print(f"- server: initialization complete.")


    def Run(self) -> None:
        print(f"- server: now running. waiting for connections.")

        while True:
            # get new connection
            connection, address = self.socket.accept()
            print(f"- server: new connection from '{address}'.")

            self.Connect_To_Game(connection, tuple(address))


    def Connect_To_Game(self, connection:socket.socket, address:tuple) -> None:

        # get settings
        settings = json.loads(connection.recv(4096).decode())

        # find valid game
        _valid_game = None
        for game in self.games:
            if game.Validate_Settings(settings):
                _valid_game = game
                break
        
        # not found
        if _valid_game == None:
            _valid_game = Game(self.Get_Game_ID(), settings)
            self.games.append(_valid_game)

        # sent game id
        connection.send(str(_valid_game.id).encode())

        # log
        print(f"- server: found game for '{address}' with id of {_valid_game.id}.")

        # create thread
        _thread.start_new_thread(self.threaded_client, (connection, address, _valid_game))




    def threaded_client(self, connection:socket.socket, address:tuple, game:Game):
        
        # log tread creation
        print(f"- server: created a thread for '{address}'.")

        while True:
            try:
                # get request
                request = json.loads(connection.recv(4096).decode())
                
                # handle request
                game.Handle(address, request)

                # return result
                connection.send(json.dumps(game.Get_Data(address)).encode())

            except Exception as e: 
                print(f"- server: lost connection with '{address}' with next error '{e}'.")
                break
        connection.close()



server = Server()
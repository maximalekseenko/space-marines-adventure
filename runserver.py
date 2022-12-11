from back import server

server.Init()
server.Run()

quit()



import socket
from _thread import *
from game.game import Game


# /-----INIT-----\
# init server socket
SERVER_ADDRESS = ("0.0.0.0", 5555)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
try: server_socket.bind(SERVER_ADDRESS)
except socket.error as e: str(e)

# start listen
server_socket.listen(2)
print("- server: initialization complete.")

# TODO:UNDERSTAND WHAT I WROTE
games = {}
idCount = 0
# \-----INIT-----/


import pickle
def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    # get new connection
    connection, address = server_socket.accept()
    print("Connected to:", address)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (connection, p, gameId))
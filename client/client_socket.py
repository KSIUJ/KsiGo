import socket


class Client:
    def __init__(self):
        self.connection = socket.socket()  # default values: ipv4, tcp
        self.user_name = ""
        self.connection.connect(('localhost', 9999))

    def set_username(self, name):
        self.user_name = name
        self.connection.send(bytes(name, 'utf-8'))
        print(self.connection.recv(1024).decode())

    def send_move(self, move):
        self.connection.send(bytes(move, 'utf-8'))

    def game(self):
        is_game = True
        while is_game:
            is_game = self.connection.recv(1024).decode()

            if is_game:
                move = input("Make a move: ")
                self.send_move(move)


# function creates a player and connects him to server
# remember that you have to create two clients to start a game
def create_player(name):
    player = Client()
    player.set_username(name)
    player.game()

import socket


class Client:
    def __init__(self, host, port):
        self.connection = socket.socket()  # default values: ipv4, tcp
        self.user_name = ""
        self.connection.connect((host, port))

    def send_message(self, message):
        parsed_message = '{:04}'.format(len(message)) + message
        self.connection.sendall(bytes(parsed_message, 'utf-8'))

    def set_username(self, name):
        self.user_name = name
        self.send_message(name)
        print(self.connection.recv(1024).decode())

    def game(self):
        is_game = True
        while is_game:
            is_game = self.connection.recv(1).decode()

            if is_game:
                move = input("Make a move: ")
                self.send_message(move)


# function creates a player and connects him to server
# remember that you have to create two clients to start a game
def create_player(name, address="localhost", port=9999):
    player = Client(address, port)
    player.set_username(name)
    player.game()

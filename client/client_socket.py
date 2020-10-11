import socket
from common import socket_utils as util


class Client:
    def __init__(self, name, host, port):
        try:
            self.client_conn = socket.socket()  # default values: ipv4, tcp
        except OSError:
            self.client_conn = None
        self.user_name = name
        self.connect(host, port)

        if self.client_conn is not None:
            self.send_username()

    def connect(self, host, port):
        try:
            self.client_conn.settimeout(None)  # just to prevent connection timeout error from the system network
            self.client_conn.connect((host, port))
        except OSError:
            self.client_conn.close()
            self.client_conn = None
            print("Could not open the socket")
            return

    def send_username(self):
        util.send_message(self.client_conn, self.user_name)

    def game(self):
        is_game = True
        while is_game:
            is_game = self.client_conn.recv(1).decode()

            if is_game:
                move = input("Make a move: ")
                util.send_message(self.client_conn, move)

        self.client_conn.close()


# function creates a player and connects him to server
# remember that you have to create two clients to start a game
def create_player(name, address="localhost", port=9999):
    player = Client(name, address, port)
    player.game()

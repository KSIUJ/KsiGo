import socket
from common import socket_utils as util


class Client:
    def __init__(self, name, host, port):
        try:
            self.client_conn = socket.socket()  # default values: ipv4, tcp
        except OSError:
            self.client_conn = None

        if self.client_conn is not None:
            self.connect(host, port)

        self.user_name = name

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
            if self.client_conn is not None:
                is_game = self.client_conn.recv(1).decode()
            else:
                is_game = False

            if is_game:
                move = input("Make a move: ")
                util.send_message(self.client_conn, move)

        if self.client_conn is not None:
            self.client_conn.close()


# function creates a player and connects him to server
# remember that you have to create two clients to start a game
def create_player(name, address="localhost", port=9999):
    player = Client(name, address, port)
    player.game()

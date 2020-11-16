import socket
from common import socket_utils as util


class Client(util.SocketCommon):
    def __init__(self, name):
        super().__init__()
        try:
            self.client_conn = socket.socket()  # default values: ipv4, tcp
        except OSError:
            self.client_conn = None

        if self.client_conn is not None:
            self.establish_connection()

        self.user_name = name

        if self.client_conn is not None:
            self.send_username()

    def establish_connection(self):
        try:
            self.client_conn.settimeout(None)  # just to prevent connection timeout error from the system network
            self.client_conn.connect((self.host, self.port))
        except OSError:
            self.client_conn.close()
            self.client_conn = None
            print("Could not open the socket")
            return

    def send_username(self):
        self.send_message(self.client_conn, self.user_name)

    def send(self, msg):
        self.send_message(self.client_conn, msg)

    def receive(self):
        return self.receive_message(self.client_conn)

    def game(self):
        is_game = True
        while is_game:
            if self.client_conn is not None:
                is_game = self.client_conn.recv(1).decode()
            else:
                is_game = False

            if is_game:
                move = input("Make a move: ")
                self.send_message(self.client_conn, move)

        if self.client_conn is not None:
            self.client_conn.close()


# function creates a player and connects him to server
# remember that you have to create two clients to start a game
def create_player(name):
    player = Client(name)
    # player.set_host_and_port("localhost", 9999) # uncomment to change default values
    player.game()

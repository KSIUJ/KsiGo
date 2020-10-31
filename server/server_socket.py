import socket
from common import socket_utils as util


class Server(util.SocketCommon):
    def __init__(self):
        super().__init__()
        try:
            self.server_conn = socket.socket()  # default values: ipv4, tcp
        except OSError:
            self.server_conn = None

        self.clients = []
        self.is_open = True

        if self.bind_with_check() is False:
            self.is_open = False
            self.close_game()

    def bind_with_check(self):
        if self.server_conn is None:
            return False

        try:
            self.server_conn.bind((self.host, self.port))
            print("Socket created")
            return True
        except OSError:
            print('Bind failed')
            return False

    def listen_for_users(self):
        while len(self.clients) < 2:
            if self.server_conn is not None:
                conn, addr = self.server_conn.accept()
                self.clients.append(conn)
                username = self.receive_message(conn)
                yield conn, addr

                print(f"Connected with {username} on address {addr}")
            else:
                return

    def create_connection(self) -> bool:
        if self.server_conn is None:
            return False

        self.server_conn.listen(2)  # buffer for two connections
        print("Waiting for connections...")

        # try:
        #     self.listen_for_users()
        # except socket.timeout:
        #     print("Failed to establish connection with 2 players (connection timeout)")
        #     self.close_game()
        #     return False

        return True

    def close_game(self):
        for user in self.clients:
            # user.send(bytes(False))
            user.close()
        if self.server_conn is not None:
            self.server_conn.close()
        self.is_open = False


# function creates a server connection for two players
def create_server():
    server = Server()
    # curr_server.set_host_and_port("localhost", 9999) # uncomment to change default values
    if server.is_open is False:
        return False
    if server.create_connection():
        # server.game()
        server.close_game()

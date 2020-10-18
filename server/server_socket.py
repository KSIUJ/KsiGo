import socket
from common import socket_utils as util


class Server:
    def __init__(self, host, port):
        try:
            self.server_conn = socket.socket()  # default values: ipv4, tcp
        except OSError:
            self.server_conn = None

        self.clients = []
        self.is_open = True
        if self.bind_with_check(host, port) is False:
            self.is_open = False
            self.close_game()

    def bind_with_check(self, host, port):
        if self.server_conn is not None:
            try:
                self.server_conn.bind((host, port))
                print("Socket created")
                return True
            except OSError:
                print('Bind failed')
                return False
        else:
            return False

    def wait_for_clients(self):
        while len(self.clients) < 2:
            if self.server_conn is not None:
                client, addr = self.server_conn.accept()
                self.clients.append(client)
                username = util.receive_message(client)

                print(f"Connected with {username} on address {addr}")
            else:
                return

    def connection(self) -> bool:
        if self.server_conn is not None:
            self.server_conn.listen(2)  # buffer for two connections
            print("Waiting for connections...")

            try:
                self.wait_for_clients()
            except socket.timeout:
                print("Failed to establish connection with 2 players (connection timeout)")
                self.close_game()
                return False

            return True
        else:
            return False

    def close_game(self):
        for user in self.clients:
            user.send(bytes(False))
            user.close()
        if self.server_conn is not None:
            self.server_conn.close()
        self.is_open = False

    def game(self):
        moves = []
        is_game = True
        player = 0
        while is_game:
            curr_player = self.clients[player]
            curr_player.send(bytes(True))

            try:
                received_move = util.receive_message(curr_player)
            except ConnectionResetError:
                # that error may happen when Windows client will be
                # closed abruptly in a TCP based program
                received_move = "error: Connection Reset Error"
                is_game = False

            if received_move[:5] == "error":
                print(f"Error: {received_move}")

            else:
                moves.append(received_move)
                print(f'Player {player} made a move: {moves[-1]}')

                player = (player + 1) % 2

                # false game ending logic
                if len(moves) == 5:
                    is_game = False


# function creates a server connection for two players
def create_server(address="localhost", port=9999):
    new_server = Server(address, port)
    if new_server.is_open is False:
        return False
    if new_server.connection():
        new_server.game()
        new_server.close_game()

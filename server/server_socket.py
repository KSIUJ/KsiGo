import socket
from common import socket_utils as util


class Server:
    def __init__(self, host, port):
        self.server_conn = socket.socket()  # default values: ipv4, tcp
        self.server_conn.bind((host, port))
        print("Socket created")
        self.clients = []

    def connection(self) -> bool:
        self.server_conn.listen(2)  # buffer for two connections
        print("Waiting for connections...")

        while len(self.clients) < 2:
            client, addr = self.server_conn.accept()
            self.clients.append(client)
            username = util.receive_message(self.clients[-1])

            print("Connected with ", username, " on address ", addr)

        return True

    def close_game(self):
        for user in self.clients:
            user.send(bytes(False))
            user.close()

    def game(self):
        moves = []
        is_game = True
        player = 0
        while is_game:
            curr_player = self.clients[player]

            curr_player.send(bytes(True))
            moves.append(util.receive_message(curr_player))
            print(f'Player {player} made a move: {moves[-1]}')

            player += 1
            player = player % 2

            # false game ending logic
            if len(moves) == 5:
                is_game = False


# function creates a server connection for two players
def create_server(address="localhost", port=9999):
    new_server = Server(address, port)
    new_server.connection()
    new_server.game()
    new_server.close_game()

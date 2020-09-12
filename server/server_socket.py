import socket


class Server:
    def __init__(self, host, port):
        self.server_conn = socket.socket()  # default values: ipv4, tcp
        self.server_conn.bind((host, port))
        print("Socket created")
        self.clients = []

    def receive_message(self, player):
        message_len = int(self.clients[player].recv(4).decode())
        message = ""

        while len(message) < message_len:
            message += self.clients[player].recv(1024).decode()

        return message

    def connection(self) -> bool:
        self.server_conn.listen(2)  # buffer for two connections
        print("Waiting for connections...")

        while len(self.clients) < 2:
            client, addr = self.server_conn.accept()
            self.clients.append(client)
            username = self.receive_message(len(self.clients) - 1)

            print("Connected with ", username, " on address ", addr)
            client.send(bytes("Welcome to ksiGo", 'utf-8'))

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
            self.clients[player].send(bytes(True))
            moves.append(self.receive_message(player))
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

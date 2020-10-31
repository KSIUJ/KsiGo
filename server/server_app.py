from socket import socket
from threading import Thread
from server.server_socket import Server as SocketServer
from common.parser import Parser
import common.game_logic as Logic


class User:
    def __init__(self, connection: socket, address: str, is_active: bool = True):
        self.connection = connection
        self.address = address
        self.is_active = is_active
        self.reader = None

    def set_reader(self, reader_thread):
        self.reader = reader_thread


class ServerApp:
    def __init__(self, host: str, port: int):
        self.socket = SocketServer()
        # self.socket.set_host_and_port(host=host, port=port)
        self.socket.create_connection()

        self.users = []

        self.parser = Parser()
        self.parser.add_module("game")
        self.parser.add_func("game", "place", self.place)

        self.board = Logic.Board(9)
        self.current_color = "black"

    def make_a_connection(self):
        for conn, addr in self.socket.listen_for_users():
            user = User(conn, addr)
            reader = Thread(target=self.read_handler,
                            args=(user, ),
                            daemon=True
                            )
            user.set_reader(reader_thread=reader)
            self.users.append(user)
            # reader.start()

    def read_handler(self, user: User):
        while user.is_active:
            msg = self.socket.receive_message(connection=user.connection)
            print(msg)

    def game(self, players: list):
        moves = []
        is_game = True
        player_id = 0
        while is_game:
            curr_player = players[player_id].connection

            # curr_player.send(bytes(True))
            move = self.socket.receive_message(curr_player)
            moves.append(move)
            print(f'Player {player_id} made a move: {self.parser.decode(move)}\n')
            self.parser.execute(move)
            for player in players:
                self.socket.send_message(player.connection, move)

            player_id = (player_id + 1) % 2

            # false game ending logic
            # if len(moves) == 5:
            #     is_game = False

    def place(self, x: int, y: int):
        self.board.update_board(x=x, y=y, color=self.current_color)
        self.current_color = 'white' if self.current_color == 'black' else 'black'
        print(f"placed on ({x}, {y})")
        self.board.print_board()


if __name__ == '__main__':

    server = ServerApp(host='localhost', port=8888)

    making_connections = Thread(target=server.make_a_connection, daemon=True)
    making_connections.start()

    while len(server.users) < 2:
        # make server stuff
        pass

    server.game(players=server.users[0:2])

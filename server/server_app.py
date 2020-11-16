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
        self.parser.add_func("game", "move", self.place)

        self.board = Logic.Board(9)
        self.current_color = "black"

    def make_a_connection(self):
        first = False
        for conn, addr, b_username in self.socket.listen_for_users():
            first = not first
            user = User(conn, addr)
            reader = Thread(target=self.read_handler,
                            args=(user, ),
                            daemon=True
                            )
            user.set_reader(reader_thread=reader)
            self.users.append(user)
            self.socket.send_message(conn, self.parser.encode_message("game", "color", first))
            # reader.start()

    def read_handler(self, user: User):
        while user.is_active:
            msg = self.socket.receive_message(connection=user.connection)
            print(msg)

    def game(self, players: list):
        is_game = True
        curr_player = players[0].connection
        receiving_player = players[1].connection
        while is_game:
            move = self.socket.receive_message(curr_player)
            self.socket.send_message(receiving_player, move)

            temp = curr_player
            curr_player = receiving_player
            receiving_player = temp

            # false game ending logic
            # if len(moves) == 5:
            #     is_game = False

    def place(self, x: int, y: int):
        if self.board.move_is_legal(x, y):
            added_stone = Logic.Stone(board=self.board, point=(x, y), color=self.board.actual_turn)
            self.board.update_liberties(added_stone=added_stone)
            self.board.update_board(x=x, y=y, color=self.board.actual_turn)

            if (x, y) != self.board.ko_beating:
                self.board.ko_beating = (-1, -1)
                self.board.ko_captive = (-1, -1)

            self.board.next_turn()


if __name__ == '__main__':

    server = ServerApp(host='localhost', port=8888)

    making_connections = Thread(target=server.make_a_connection, daemon=True)
    making_connections.start()

    while len(server.users) < 2:
        # make server stuff
        pass

    server.game(players=server.users[0:2])
import sys
import threading

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, QObject

from client.interfaces.client import IClient
from client.gui.windows import MainWindow
from client.client_socket import Client as ClientSocket
from common.parser import Parser


class Client(IClient):

    class OpponentsRespondHandler(QObject):
        opponent_move_signal = Signal(int, int)
        opponent_pass_signal = Signal()
        opponent_resign_signal = Signal()

    def __init__(self):
        self.app = None
        self.passes = 0
        self.username = None
        self.my_turn: bool = True
        self.socket = None
        self.game_window = None
        self.receiving_thread = threading.Thread(target=self.other_player, daemon=True)

        self.opponent_handler = self.OpponentsRespondHandler()

        self.parser = Parser()
        self.parser.add_module("game")
        self.parser.add_func("game", "move", self.on_opponent_moved)
        self.parser.add_func("game", "pass", self.on_opponent_passed)
        self.parser.add_func("game", "resign", self.on_opponent_resigned)
        self.parser.add_func("game", "color", self.set_first_player)

    def encode_move(self, x: int, y: int) -> bytes:
        return self.parser.encode_message("game", "move", x, y)

    def encode_pass(self) -> bytes:
        return self.parser.encode_message("game", "pass")

    def encode_resign(self) -> bytes:
        return self.parser.encode_message("game", "resign")

    def encode_username(self) -> bytes:
        return self.parser.encode_message("game", "username", self.username)

    def is_my_turn(self) -> bool:
        return self.my_turn

    def on_username_provided(self, username: str):
        self.username = username

    def check_double_pass(self):
        self.my_turn = not self.my_turn
        self.passes += 1
        if self.passes >= 2:
            return True
        return False

    def get_passes(self) -> int:
        return self.passes

    def on_pass_clicked(self):
        self.socket.send(self.encode_pass())

    def on_pawn_put(self, x: int, y: int):
        self.passes = 0
        self.my_turn = False
        self.socket.send(self.encode_move(x, y))

    def on_resign_confirmed(self):
        self.socket.send(self.encode_resign())

    def on_opponent_moved(self, x: int, y: int):
        self.opponent_handler.opponent_move_signal.emit(x, y)
        self.my_turn = True
        self.passes = 0

    def on_opponent_passed(self):
        self.opponent_handler.opponent_pass_signal.emit()

    def on_opponent_resigned(self):
        self.opponent_handler.opponent_resign_signal.emit()

    def on_game_window_opened(self, size: int):
        self.socket = ClientSocket(self.encode_username())
        self.get_color()
        self.receiving_thread.start()

    def set_first_player(self, black: bool):
        self.my_turn = black

    def open(self, stacked_page=0):
        window = MainWindow(self)
        window.ui.stackedWidget.setCurrentIndex(stacked_page)

    def get_color(self):
        msg = self.socket.receive()
        self.parser.execute(msg)

    def other_player(self):
        while True:
            msg = None
            msg = self.socket.receive()

            if msg:
                self.parser.execute(msg)

    def start(self):
        self.app = QApplication()
        self.open()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    client = Client()
    client.start()

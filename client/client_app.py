import sys

from threading import Thread
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, QObject

from client.interfaces.client import IClient
from client.gui.windows import MainWindow
from client.client_socket import Client as ClientSocket
from common.parser import Parser, ParsingError


class Client(IClient):

    class SignalController(QObject):
        board_update_signal = Signal(int, int)

    def __init__(self):
        self.app = None
        self.passes = 0
        self.socket = ClientSocket('nameless')
        # self.socket.set_host_and_port("0.0.0.0", 9999)
        # self.socket.establish_connection()
        self.parser = Parser()
        self.parser.add_module("game")
        self.parser.add_func("game", "place", self.place)

        self.color = None
        self.controller = self.SignalController()
        Thread(target=self.read_handler, daemon=True).start()

    def setColor(self, color: str):
        self.color = color

    def on_username_provided(self, username: str):
        pass

    def on_pass_clicked(self):
        self.passes += 1
        if self.passes == 2:
            return True
        return False

    def on_pawn_put(self, x: int, y: int):
        self.socket.send_msg(self.parser.encode_message("game", "place", x=x, y=y))
        self.passes = 0

    def on_resign_confirmed(self):
        self.app.exit(0)

    def open(self, stacked_page=0):
        window = MainWindow(self)
        window.ui.stackedWidget.setCurrentIndex(stacked_page)

    def start(self):
        self.app = QApplication()
        self.open()
        sys.exit(self.app.exec_())

    def read_handler(self):
        while(True):
            move = self.socket.recv_msg()
            if move:
                self.parser.execute(move)
            move = None

    def place(self, x: int, y: int):
        self.controller.board_update_signal.emit(x, y)


if __name__ == '__main__':
    client = Client()
    # client.setColor("white" if input('type [b/w] for black or white:\n_>') else 'black')
    client.start()

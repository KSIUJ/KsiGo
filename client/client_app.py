import sys

from PySide2.QtWidgets import QApplication

from client.interfaces.client import IClient
from client.gui.windows import MainWindow


class Client(IClient):

    def __init__(self):
        self.app = None
        self.passes = 0

    def on_username_provided(self, username: str):
        pass

    def on_pass_clicked(self):
        self.passes += 1
        if self.passes == 2:
            return True
        return False

    def on_pawn_put(self):
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


if __name__ == '__main__':
    client = Client()
    client.start()

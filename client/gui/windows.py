import OpenGL.GL as gl
import PySide2

from PySide2.QtWidgets import QMainWindow, QMessageBox, QOpenGLWidget, QVBoxLayout, QDialog, QLabel
from PySide2.QtGui import QMouseEvent
from client.gui.ui_main_window import Ui_MainWindow
from client.gui.ui_game_window import Ui_GameWindow
from client.gui.ui_end_dialog import Ui_Dialog
from client.interfaces.client import IClient
from common.game_logic import *


class MainWindow(QMainWindow):
    def __init__(self, events: IClient):
        super().__init__()

        self.events = events

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Ksi Go")

        self.game = None

        self.ui.start_button.clicked.connect(self.start)
        self.ui.connect_button.clicked.connect(self.check_username)
        self.ui.x9_button.clicked.connect(lambda: self.play(9))
        self.ui.x13_button.clicked.connect(lambda: self.play(13))
        self.ui.x19_button.clicked.connect(lambda: self.play(19))

        self.ui.stackedWidget.setCurrentWidget(self.ui.welcome_screen)

        self.show()

    def start(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.board_size_screen)

    def check_username(self):
        username = self.ui.username_input.toPlainText()
        if 3 <= len(username) <= 20:
            self.ui.stackedWidget.setCurrentWidget(self.ui.board_size_screen)
        else:
            self.ui.username_input.clear()
            box = QMessageBox()
            box.setText("Provided username does not have required length")
            box.setWindowTitle("Wrong username")
            box.setIcon(QMessageBox.Warning)
            box.exec()

    def play(self, size):
        self.game = GameWindow(size, self.events)
        self.close()


class GlWidget(QOpenGLWidget):

    def __init__(self, size, events: IClient):
        super().__init__()
        self.my_turn = False
        self.size = size
        self.events = events
        self.window_size = 0.9
        self.board = Board(size)

    def initializeGL(self):
        super().initializeGL()

    def resizeGL(self, w: int, h: int):
        super().resizeGL(w, h)

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glColor3f(0.8, 0.6, 0.3)
        gl.glRectf(-1, -1, 1, 1)

        step = (2 * self.window_size / (self.size - 1))

        for i in range(self.size):
            gl.glColor3f(0, 0, 0)
            gl.glLineWidth(3)

            index = i * step
            gl.glBegin(gl.GL_LINES)
            gl.glVertex2f(-self.window_size + index, -self.window_size)
            gl.glVertex2f(-self.window_size + index, self.window_size)
            gl.glEnd()

            gl.glBegin(gl.GL_LINES)
            gl.glVertex2f(-self.window_size, -self.window_size + index)
            gl.glVertex2f(self.window_size, -self.window_size + index)
            gl.glEnd()

        if self.size == 19:
            point_size = 0.05
        elif self.size == 13:
            point_size = 0.07
        else:
            point_size = 0.1

        gl.glPointSize(min(self.width(), self.height()) * point_size)

        for i in range(self.size):
            gl.glEnable(gl.GL_POINT_SMOOTH)
            for j in range(self.size):
                if self.board.Matrix[i][j] == 'b':
                    gl.glColor3f(0, 0, 0)

                    gl.glBegin(gl.GL_POINTS)
                    gl.glVertex2f(-self.window_size + (j * step), self.window_size - (i * step))
                    gl.glEnd()

                elif self.board.Matrix[i][j] == 'w':
                    gl.glColor3f(1, 1, 1)

                    gl.glBegin(gl.GL_POINTS)
                    gl.glVertex2f(-self.window_size + (j * step), self.window_size - (i * step))
                    gl.glEnd()

    def mousePressEvent(self, event: QMouseEvent):
        pos = event.pos()

        x = ((-self.width() / 2) + pos.x()) / (self.window_size * self.width() / 2)
        y = -((self.height() / 2) - pos.y()) / (self.window_size * self.height() / 2)

        index_x = 0
        index_y = 0

        diff = 2
        for index in range(self.size):
            i = -1 + (index * (2 / (self.size - 1)))
            if abs(x - i) < diff:
                index_x = index
                diff = abs(x - i)

        diff = 2
        for index in range(self.size):
            i = -1 + (index * (2 / (self.size - 1)))
            if abs(y - i) < diff:
                index_y = index
                diff = abs(y - i)

        if self.board.move_is_legal(index_y, index_x):
            added_stone = Stone(board=self.board, point=(index_y, index_x), color=self.board.actual_turn)
            self.board.update_liberties(added_stone=added_stone)
            self.board.update_board(x=index_y, y=index_x, color=self.board.actual_turn)

            if (index_y, index_x) != self.board.ko_beating:
                self.board.ko_beating = (-1, -1)
                self.board.ko_captive = (-1, -1)

            self.board.next_turn()
            self.events.on_pawn_put()
        else:
            print('error')

        self.update()

    def get_points(self):
        return self.board.count_points()


class GameWindow(QMainWindow):
    def __init__(self, size, events: IClient):
        super().__init__()

        self.size = size
        self.events = events

        self.dialog = None

        self.ui = Ui_GameWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Ksi Go")

        layout = QVBoxLayout()
        self.gl_widget = GlWidget(size, events)
        layout.addWidget(self.gl_widget)
        self.ui.opengl_container.setLayout(layout)

        self.ui.pass_button.clicked.connect(self.pass_)
        self.ui.resign_button.clicked.connect(self.resign)

        self.show()

    def pass_(self):
        if self.events.on_pass_clicked():
            black, white = self.gl_widget.get_points()
            diff = abs(black - white)
            if black > white:
                text = f"Player with black pawns won having {diff} more points"
            else:
                text = f"Player with white pawns won having {diff} more points"
            self.dialog = EndGameDialog(text, self, self.events)
        self.gl_widget.board.next_turn()

    def resign(self):
        # window
        print('lost')


class EndGameDialog(QDialog):
    def __init__(self, text, game_window: QMainWindow, events: IClient):
        super().__init__()

        self.game_window = game_window
        self.events = events

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Game ended")
        self.ui.end_text.setText(text)
        self.ui.play_again_button.clicked.connect(self.play_again)
        self.show()

    def play_again(self):
        self.game_window.close()
        self.close()
        self.events.open()

    def closeEvent(self, arg__1: PySide2.QtGui.QCloseEvent):
        super().closeEvent(arg__1)
        self.game_window.close()

import sys
import OpenGL.GL as gl
from math import fabs
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QOpenGLWidget, QVBoxLayout
from PySide2.QtGui import QMouseEvent
from gui.ui_main_window import Ui_MainWindow
from gui.ui_game_window import Ui_GameWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Ksi Go")

        self.ui.start_button.clicked.connect(self.start)
        self.ui.connect_button.clicked.connect(self.check_username)
        self.ui.x9_button.clicked.connect(self.play_9)
        self.ui.x13_button.clicked.connect(self.play_13)
        self.ui.x19_button.clicked.connect(self.play_19)

        self.ui.stackedWidget.setCurrentWidget(self.ui.welcome_screen)

        self.show()

    def start(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.username_screen)

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

    def play_9(self):
        self.game = GameWindow(9)
        self.game.show()
        self.close()

    def play_13(self):
        self.game = GameWindow(13)
        self.game.show()
        self.close()

    def play_19(self):
        self.game = GameWindow(19)
        self.game.show()
        self.close()


class GlWidget(QOpenGLWidget):

    def __init__(self, size):
        super().__init__()
        self.size = size
        self.board = [['*' for _ in range(size)] for _ in range(size)]

    def initializeGL(self):
        super().initializeGL()

    def resizeGL(self, w: int, h: int):
        super().resizeGL(w, h)

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glColor3f(0.8, 0.6, 0.3)
        gl.glRectf(-1, -1, 1, 1)

        step = (1.9 / (self.size - 1))

        for i in range(self.size):
            gl.glColor3f(0, 0, 0)
            gl.glLineWidth(3)

            index = i * (1.9 / (self.size - 1))
            gl.glBegin(gl.GL_LINES)
            gl.glVertex2f(-0.95 + index, -0.95)
            gl.glVertex2f(-0.95 + index, 0.95)
            gl.glEnd()

            gl.glBegin(gl.GL_LINES)
            gl.glVertex2f(-0.95, -0.95 + index)
            gl.glVertex2f(0.95, -0.95 + index)
            gl.glEnd()

            gl.glEnable(gl.GL_POINT_SMOOTH)
            for j in range(self.size):
                if self.board[i][j] == 'b':
                    gl.glColor3f(1, 1, 1)
                    gl.glPointSize(30)

                    gl.glBegin(gl.GL_POINTS)
                    gl.glVertex2f(-0.95+(j*step), 0.95-(i*step))
                    gl.glEnd()

                elif self.board[i][j] == 'c':
                    gl.glColor3f(0, 0, 0)
                    gl.glPointSize(30)

                    gl.glBegin(gl.GL_POINTS)
                    gl.glVertex2f(-0.95+(j*step), 0.95-(i*step))
                    gl.glEnd()

    def mousePressEvent(self, event: QMouseEvent):
        pos = event.pos()

        x = (pos.x() - (0.025 * self.width())) / self.width()
        y = (pos.y() - (0.025 * self.height())) / self.height()

        index_x = 0
        index_y = 0

        diff = 2
        for index in range(self.size):
            i = index * (1 / self.size)
            if fabs(x - i) < diff:
                index_x = index
            diff = x - i

        diff = 2
        for index in range(self.size):
            i = index * (1 / self.size)
            if fabs(y - i) < diff:
                index_y = index
            diff = y - i

        self.board[index_y][index_x] = 'b'
        self.update()


class GameWindow(QMainWindow):
    def __init__(self, size):
        super().__init__()

        self.ui = Ui_GameWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Ksi Go")

        layout = QVBoxLayout()
        widget = GlWidget(size)
        layout.addWidget(widget)
        self.ui.opengl_container.setLayout(layout)

        self.show()


def start():
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec_())

import sys
import OpenGL.GL as Gl
import PySide2.QtWidgets as Qtw
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore


class gameWindow(Qtw.QOpenGLWidget):

    def __init__(self, size):
        Qtw.QOpenGLWidget.__init__(self)
        self.size = size
        self.board = [['*' for _ in range(size)] for _ in range(size)]
        # self.event = Qgui.QKeyEvent()

    def initializeGL(self):
        Gl.glClearColor(0.3, 0.3, 0.3, 0.3)

    def resizeGl(self, width, heigh):
        Gl.glViewport(0, 0, width, heigh)

    def paintGL(self):
        Gl.glClear(Gl.GL_COLOR_BUFFER_BIT)
        Gl.glColor3f(0.8, 0.6, 0.3)
        board_size = self.size / 10 + 0.1
        Gl.glRectf(-board_size, -board_size, board_size, board_size)

        Gl.glColor3f(0, 0, 0)
        Gl.glLineWidth(5)
        for i in range(-self.size, self.size + 1, 1):
            # Vertical lines
            Gl.glBegin(Gl.GL_LINES)
            Gl.glVertex2f(i / 10, -self.size / 10)
            Gl.glVertex2f(i / 10, self.size / 10)
            Gl.glEnd()
            # Horizontal Lines
            Gl.glBegin(Gl.GL_LINES)
            Gl.glVertex2f(-self.size / 10, i / 10)
            Gl.glVertex2f(self.size / 10, i / 10)
            Gl.glEnd()

        Gl.glPointSize(40)
        Gl.glEnable(Gl.GL_POINT_SMOOTH)
        for y, row in enumerate(self.board):
            for x, pawn in enumerate(row):
                if pawn != '*':
                    color = (0, 0, 0) if pawn == 'b' else (1, 1, 1)
                    Gl.glColor3f(*color)

                    Gl.glBegin(Gl.GL_POINTS)
                    Gl.glVertex2f((x + 1) / 10 - 1, -(y + 1) / 10 + 1)
                    Gl.glEnd()
        Gl.glFlush()

    def put_pawn(self, position: tuple, color: str):
        if color not in ('white', 'black'):
            raise Exception('color can be only white or black')
        try:
            x, y = position
        except ValueError:
            raise ValueError('position should be pass as (x, y)')

        self.board[y][x] = 'b' if color == 'black' else 'w'

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            for y, row in enumerate(self.board):
                for x, pawn in enumerate(row):
                    self.board[y][x] = '*'
        self.update()

    def mousePressEvent(self, event):
        pos = event.pos()
        x = int(pos.x() / self.width() * 10)
        y = int(pos.y() / self.height() * 10)
        self.put_pawn((x, y), 'black')
        print(f'({x}, {y})')
        self.update()


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)

    game = gameWindow(9)
    game.resize(1200, 900)

    game.put_pawn(position=(1, 2), color='white')

    game.show()
    sys.exit(app.exec_())
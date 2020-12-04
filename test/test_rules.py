import sys
import io
from contextlib import redirect_stdout
from common import game_logic


class TestKSIGO1:
    def setup(self):
        self.board = game_logic.Board(size=4)

    def test_empty_board(self):
        return self.board, [["****"], ["****"], ["****"], ["****"]]

    def test_starting_player(self):
        return self.board.actual_turn, "black"

    def test_next_turn(self):
        self.board.next_turn()
        return self.board.actual_turn, "white"


class TestKSIGO2:
    def setup(self):
        self.board = game_logic.Board(size=5)
        self.output = None

        # make some moves with passing
        with io.StringIO() as buf, redirect_stdout(buf):
            self.board.lets_play()
            # col X
            # row Y
            i_x = 3
            i_y = 3

            sys.stdin = str(i_x - 1)
            sys.stdin = str(i_y)

            sys.stdin = "PASS"

            sys.stdin = str(i_x)
            sys.stdin = str(i_y - 1)

            sys.stdin = "PASS"

            sys.stdin = str(i_x)
            sys.stdin = str(i_y + 1)

            sys.stdin = str(i_x)
            sys.stdin = str(i_y)

            sys.stdin = str(i_x + 1)
            sys.stdin = str(i_y)

            buf.getvalue()  # clear output
            self.board.print_board()
            self.output = buf.getvalue()

    def test_board(self):
        return self.output, \
               [
                   ["*****"],
                   ["***b*"],
                   ["**b*b"],
                   ["***b*"],
                   ["*****"]
               ]

    def test_points(self):
        print(self.board.count_points())
        return self.board.count_points(), 345


t = TestKSIGO2()
t.setup()
print(t.test_points())
print(t.board.print_board())
print(t.board.passed_turn)

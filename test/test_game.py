import random
import sys

from common import game_logic
from test import utils
import io
from contextlib import redirect_stdout


class TestPrinting:

    # no points testing
    def test_points_counting(self):
        t1 = game_logic.Board()
        return t1.count_points(), (0, 7.5)

    # both players only pass since the beginning
    def test_some_passing(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            t1 = game_logic.Board()

            passes = random.randint(1, 10)
            for i in range(0, passes):
                sys.stdin = "PASS"

            buf.getvalue()
            t1.print_board()
            output = buf.getvalue()
        return output, utils.get_empty_board()

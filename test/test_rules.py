import sys
import io
from contextlib import redirect_stdout

import pytest

from common import game_logic
from test import utils


# game beginning KSIGO-1
# @pytest.fixture(autouse=True)
# def board():
#     return game_logic.Board(size=4)


class TestGameBeginning:
    def setup(self):
        self.board = game_logic.Board(size=4)

    def test_empty_board(self):
        return self.board, [["****"], ["****"], ["****"], ["****"]]

    def test_starting_player(self):
        return self.board.actual_turn, "black"

    def test_next_turn(self):
        self.board.next_turn()
        return self.board.actual_turn, "white"

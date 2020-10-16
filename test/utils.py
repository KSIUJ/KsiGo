import io
from contextlib import redirect_stdout
from common import game_logic


# saving the empty board printing to file
def get_empty_board():
    with io.StringIO() as buf, redirect_stdout(buf):
        t1 = game_logic.Board()
        t1.print_board()
        output = buf.getvalue()
    return output

from enum import Enum
import re


class EventType(Enum):
    EXIT = 0
    MOVE = 1


def get_event() -> (EventType, tuple):
    msg = "Make a move or type 'exit' to quit.\n" \
          "Move should look like this: 'x,y', where x and y are integers in range <1,19>\n"

    while True:
        _input = input(msg)
        if _input == "exit":
            event = EventType.EXIT
            break
        elif is_move_formatted_right(_input):
            event = EventType.MOVE
            (x, _, y) = _input.partition(",")
            _input = (int(x), int(y))
            break
        else:
            print("Try again\n")

    return event, _input


def is_move_formatted_right(move: str):
    match = False
    if re.match("^[1-9][,][1-9]$", move):
        match = True
    elif re.match("^[1-9][,][1][0-9]$", move):
        match = True
    elif re.match("^[1][0-9][,][1-9]$", move):
        match = True
    elif re.match("^[1][0-9][,][1][0-9]$", move):
        match = True

    return match

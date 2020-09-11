from enum import Enum
import re


class EventType(Enum):
    EXIT = 0
    MOVE = 1


def get_event() -> (EventType, str):
    msg = "Make a move or type 'exit' to quit.\n" \
          "Move should look like this: 'x,y', where x and y are integers in range <1,15>\n"

    while True:
        text = input(msg)
        if text == "exit":
            event = EventType.EXIT
            break
        elif is_move_formatted_right(text):
            event = EventType.MOVE
            break
        else:
            print("Try again\n")

    return event, text


def is_move_formatted_right(move: str):
    match = False
    if re.match("^[1-9][,][1-9]$", move):
        match = True
    elif re.match("^[1-9][,][1][0-5]$", move):
        match = True
    elif re.match("^[1][0-5][,][1-9]$", move):
        match = True
    elif re.match("^[1][0-5][,][1][0-5]$", move):
        match = True

    return match


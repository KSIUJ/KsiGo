class Parser:
    separator = ""
    binds = {}
    @classmethod
    def execute(cls, command: str):
        (pref, _, suff) = command.partition(cls.separator)
        cls.binds[pref](suff)

    @staticmethod
    def remove_parenthesis(string: str) -> str:
        if string.startswith("("):
            string = string.lstrip("(")
        if string.endswith(")"):
            string = string.rstrip(")")
        return string

    @classmethod
    def extract_args(cls, types: tuple, arg_string: str) -> list:
        ret_tuple = list()
        arg_string = cls.remove_parenthesis(arg_string)
        for type_ in types:
            (arg, _, arg_string) = arg_string.partition(",")
            arg = arg.strip()
            arg_string = arg_string.strip()
            ret_tuple.append(type_(arg))
        return ret_tuple

class GameParserHelper:
    @classmethod
    def place(cls, args: str):
        [x, y] = Parser.extract_args((int, int), args)
        print(f"This command places a stone on a board at coordinates ({x}, {y})")

class GameParser(Parser):
    separator = "("
    binds = {
        "place": GameParserHelper.place
    }
    @classmethod
    def place(cls, x: int,y: int) -> str:
        return "game.place({x}, {y})"


class MainParser(Parser):
    separator = "."
    parsers = {
        "game": GameParser
    }
    # binds = {string: parser.execute for (string, parser) in parsers.items()}
    binds = {
        "game": GameParser.execute
    }

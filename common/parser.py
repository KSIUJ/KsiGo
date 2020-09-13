class Parser:
    separator = ""
    binds = {}
    @classmethod
    def execute(cls, command: str):
        (pref, _, suff) = command.partition(cls.separator)
        cls.binds[pref](suff)
    @classmethod
    def extract_args(cls, types, arg_strings: str):
        ret_tuple = list()
        arg_string = arg_strings
        if arg_string.startswith("("):
            arg_string = arg_string.lstrip("(")
        if arg_string.endswith(")"):
            arg_string = arg_string.rstrip(")")
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

class MainParser(Parser):
    separator = "."
    parsers = {
        "game": GameParser
    }
    # binds = {string: parser.execute for (string, parser) in parsers.items()}
    binds = {
        "game": GameParser.execute
    }

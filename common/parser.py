import pickle
import typing


class ParsingError(KeyError):
    def __init__(self):
        super().__init__(self)


class Message:
    def __init__(self, module: str, func: str, args: tuple):
        self.module = module
        self.func = func
        self.args = args


class Parser:
    def __init__(self):
        self.bindings = {}

    def add_module(self, module_name: str):
        self.bindings[module_name] = {}

    def add_func(self, module: str, func_name: str, func: typing.Callable):
        self.bindings[module][func_name] = func

    def execute(self, command: bytes):
        command = self.decode(command)
        try:
            self.bindings[command.module][command.func](command.args)
        except KeyError as e:
            pe = ParsingError(e)
            raise pe

    @staticmethod
    def encode(mssg: Message) -> bytes:
        return pickle.dumps(mssg)

    @staticmethod
    def encode_message(module: str, func: str, args: tuple) -> bytes:
        return encode(Message(module, func, args))

    @staticmethod
    def decode(mssg: bytes) -> Message:
        return pickle.loads(mssg)

# Example code that uses Parser


class GameCommandManager:
    def __init__(self):
        parser = Parser()
        parser.add_module("game")
        parser.add_func("game", "place", self.place)
        self.parser = parser

    @staticmethod
    def place(args: tuple):
        (x, y) = args
        print(
            f"This command places a stone on a board at coordinates ({x}, {y})")

    def encode_place(self, x: int, y: int) -> bytes:
        return self.parser.encode_message("game", "place", (x, y))


if __name__ == "__main__":
    gcm = GameCommandManager()
    gcm.parser.execute(gcm.encode_place(12, 13))

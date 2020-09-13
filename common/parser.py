import pickle


class Message:
    def __init__(self, func, args: tuple):
        super().__init__()
        self.func = func
        self.args = args


class Parser:
    @classmethod
    def execute(cls, command: bytes):
        command = cls.decode(command)
        command.func(command.args)

    @classmethod
    def encode(cls, mssg: Message) -> bytes:
        return pickle.dumps(mssg)

    @classmethod
    def decode(cls, mssg: bytes) -> Message:
        return pickle.loads(mssg)


class GameCommandManager(Parser):
    @classmethod
    def place(cls, args: tuple):
        (x, y) = args
        print(
            f"This command places a stone on a board at coordinates ({x}, {y})")

    @classmethod
    def encode_place(cls, x: int, y: int) -> bytes:
        return cls.encode(Message(GameCommandManager.place, (x, y)))

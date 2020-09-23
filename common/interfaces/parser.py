import abc


class IMessage(metaclass=abc.ABCMeta):
    # package of communication data
    pass


class IParser(metaclass=abc.ABCMeta):
    # parsing messages from socket communication

    @classmethod
    @abc.abstractmethod
    def execute(cls, command: bytes):
        pass

    @classmethod
    @abc.abstractmethod
    def encode(cls, mssg: IMessage) -> bytes:
        pass

    @classmethod
    @abc.abstractmethod
    def decode(cls, mssg: bytes) -> IMessage:
        pass

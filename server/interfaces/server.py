import abc


class IServer(metaclass=abc.ABCMeta):
    # Ṃain server class

    @abc.abstractmethod
    def make_connections(self, connection):
        pass

    @abc.abstractmethod
    def read_handler(self, connection, message):
        pass


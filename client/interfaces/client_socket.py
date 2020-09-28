import abc


class IClientSocket(metaclass=abc.ABCMeta):
    #  Client side of socket communication

    @abc.abstractmethod
    def receive_message(self, connection):
        pass

    @abc.abstractmethod
    def send_message(self, connection, message):
        pass

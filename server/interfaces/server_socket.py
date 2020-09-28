import abc


class IServerSocket(metaclass=abc.ABCMeta):
    #  Server side of socket communication

    @abc.abstractmethod
    def receive_message(self, connection):
        pass

    @abc.abstractmethod
    def send_message(self, connection, message):
        pass

    @abc.abstractmethod
    def listen_for_users(self):
        pass

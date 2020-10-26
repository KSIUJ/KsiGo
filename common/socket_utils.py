import struct


class SocketCommon:
    def __init__(self):
        self.host = "localhost"
        self.port = 9999

    def set_host_and_port(self, host, port):
        self.host = host
        self.port = port

    def receive_message(self, connection) -> bytes:
        message_len = struct.unpack('i', connection.recv(4))[0]
        message = b""

        while len(message) < message_len:
            chunk = connection.recv(1024)
            if chunk:
                message += chunk

        print(f"     received < {message_len} | {message}")
        return message

    def send_message(self, connection, message: bytes):
        parsed_message = struct.pack('i', len(message)) + message
        print(f"     send > {message}")
        connection.sendall(parsed_message)

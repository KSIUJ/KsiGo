import struct


class SocketCommon:
    def __init__(self):
        self.host = "localhost"
        self.port = 9999

    def set_host_and_port(self, host, port):
        self.host = host
        self.port = port

    def receive_message(self, connection):
        message_len = struct.unpack('i', bytes(connection.recv(4).decode(), 'utf-8'))[0]
        message = ""

        while len(message) < message_len:
            chunk = connection.recv(1024)
            if chunk:
                message += chunk.decode()

        print(f"     received < {message_len} | {message}")
        return message

    def send_message(self, connection, message):
        parsed_message = struct.pack('i', len(message)) + bytes(message, 'utf-8')
        print(f"     send > {message}")
        connection.sendall(parsed_message)

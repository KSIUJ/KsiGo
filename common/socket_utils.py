import struct


def receive_message(connection):
    message_len = struct.unpack('i', bytes(connection.recv(4).decode(), 'utf-8'))[0]
    message = ""

    while len(message) < message_len:
        message += connection.recv(1024).decode()

    return message


def send_message(connection, message):
    parsed_message = struct.pack('i', len(message)) + bytes(message, 'utf-8')
    print(parsed_message)
    connection.sendall(parsed_message)

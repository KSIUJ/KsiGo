def receive_message(connection):
    message_len = int(connection.recv(4).decode())
    message = ""

    while len(message) < message_len:
        message += connection.recv(1024).decode()

    return message


def send_message(connection, message):
    parsed_message = '{:04}'.format(len(message)) + message
    connection.sendall(bytes(parsed_message, 'utf-8'))

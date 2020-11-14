import argparse
import threading

import common.parser
import common.game_logic
import server.server_socket
import server.interfaces.server_socket
import server.interfaces.server


class Server(IServer):

    def __init__(self, cli_parser: argparse.ArgumentParser):
        args = cli_parser.parse_args()
        print(args)
        self.defaultPort = args.port
        self.player_cap = args.player_cap
        self.readers = []
        self.players = []
        self.socket = IServerSocket()

    @classmethod
    def getAppParser(cls) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser()
        parser.add_argument("--port", type=int, default=19995)
        parser.add_argument("--player-cap", type=int, default=2)
        return parser

    def run(self):
        pass

    def read_handler(self, connection, message):
        connection
        pass

    def make_connections(self, connection):
        for conn in self.socket.listen_for_users():
            t = threading.Thread(self.read_handler(conn))
            self.readers.append(t)
            t.start()



def main():
    app = Server(Server.getAppParser())
    app.run()


if(__name__ == "__main__"):
    main()

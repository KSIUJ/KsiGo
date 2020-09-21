import argparse
# import common.parser
# import common.game_logic
# import server.server_socet


class App:

    def __init__(self, parser: argparse.ArgumentParser):
        args = parser.parse_args()
        print(args)
        self.defaultPort = args.port
        self.server_cap = args.server_cap
        self.servers = []

    @classmethod
    def getAppParser(cls) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser()
        parser.add_argument("--port", type=int, default=19995)
        parser.add_argument("--server-cap", type=int, default=1)
        return parser

    def run(self):
        while len(self.servers) < self.server_cap:
            new_server = Server("localhost", self.defaultPort)
            self.servers.append(new_server)
            new_server.connection()
            new_server.game()
            new_server.close_game()


def main():
    app = App(App.getAppParser())
    app.run()


if(__name__ == "__main__"):
    main()

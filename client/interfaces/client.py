from abc import ABC, abstractmethod


class IClient(ABC):

    opponent_handler = None

    @abstractmethod
    def on_username_provided(self, username: str):
        pass

    @abstractmethod
    def check_double_pass(self) -> bool:
        pass

    @abstractmethod
    def on_pass_clicked(self):
        pass

    @abstractmethod
    def on_resign_confirmed(self):
        pass

    @abstractmethod
    def on_pawn_put(self, x: int, y: int):
        pass

    @abstractmethod
    def open(self, stacked_page=0):
        pass

    @abstractmethod
    def is_my_turn(self) -> bool:
        pass

    @abstractmethod
    def on_game_window_opened(self, size: int):
        pass

    @abstractmethod
    def is_game(self) -> bool:
        pass

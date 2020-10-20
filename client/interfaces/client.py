from abc import ABC, abstractmethod


class IClient(ABC):
    @abstractmethod
    def on_username_provided(self, username: str):
        pass

    @abstractmethod
    def on_pass_clicked(self) -> bool:
        pass

    @abstractmethod
    def on_resign_confirmed(self):
        pass

    @abstractmethod
    def on_pawn_put(self):
        pass

    @abstractmethod
    def open(self, stacked_page=0):
        pass

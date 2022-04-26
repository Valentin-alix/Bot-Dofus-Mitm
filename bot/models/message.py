from bot.models.data import Data


class Message:
    def __init__(self, message_id: int = None, data: Data = None):
        self.__message_id: int = message_id
        self.__data: Data = data

    @property
    def message_id(self) -> int:
        return self.__message_id

    @property
    def data(self) -> Data:
        return self.__data

from models.data import Data


class ExchangeObjectAddedMessage:
    @staticmethod
    def deserialize(data: Data):
        return None

    def on_receive(message):
        print(message)

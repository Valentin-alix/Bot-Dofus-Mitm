from network.parsed_message.parsed_message_client.parsed_message_client import (
    ParsedMessageClient,
)


class ExchangeObjectMovePricedMessage(ParsedMessageClient):
    objectUID: int
    price: int
    quantity: int

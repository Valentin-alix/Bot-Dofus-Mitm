from network.parsed_message.parsed_message_client.parsed_message_client import (
    ParsedMessageClient,
)


class ExchangeBidHouseTypeMessage(ParsedMessageClient):
    """When checking category hdv, from client"""

    follow: bool
    type: int

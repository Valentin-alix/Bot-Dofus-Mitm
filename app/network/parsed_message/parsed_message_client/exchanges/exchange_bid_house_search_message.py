from network.parsed_message.parsed_message_client.parsed_message_client import (
    ParsedMessageClient,
)


class ExchangeBidHouseSearchMessage(ParsedMessageClient):
    """When clicking object hdv, from client"""

    follow: bool
    objectGID: int

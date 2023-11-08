from __future__ import annotations

from network.parsed_message.parsed_message_client.parsed_message_client import (
    ParsedMessageClient,
)


class ExchangeBidHousePriceMessage(ParsedMessageClient):
    """from client"""

    objectGID: int

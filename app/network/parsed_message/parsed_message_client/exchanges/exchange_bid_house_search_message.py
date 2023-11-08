from __future__ import annotations

import network.parsed_message.parsed_message_client.parsed_message_client as parsed_message_client


class ExchangeBidHouseSearchMessage(parsed_message_client.ParsedMessageClient):
    """When clicking object hdv, from client"""

    follow: bool
    objectGID: int

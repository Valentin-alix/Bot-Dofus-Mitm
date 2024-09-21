from datetime import datetime
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from app.interfaces.models.common import ParsedMessage


class ParsedMessageInfo(TypedDict):
    parsed_msg: "ParsedMessage"
    from_client: bool
    time: datetime

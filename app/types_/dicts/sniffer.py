from datetime import datetime
from typing import TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from app.types_.models.common import ParsedMessage


class ParsedMessageInfo(TypedDict):
    parsed_msg: 'ParsedMessage'
    from_client: bool
    time: datetime

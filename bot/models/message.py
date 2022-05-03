from dataclasses import dataclass
from bot.models.data import Data


@dataclass
class Message:
    message_id: int = None
    data: Data = None

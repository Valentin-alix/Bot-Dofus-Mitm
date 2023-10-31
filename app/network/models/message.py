from dataclasses import dataclass
from typing import Optional


@dataclass
class Message:
    message_type: str
    content: Optional[dict] = None

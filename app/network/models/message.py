from dataclasses import dataclass
from typing import Optional


@dataclass
class Message:
    message_type: str
    from_client: bool
    content: Optional[dict] = None

from dataclasses import dataclass, field


@dataclass
class Item:
    name: str = None
    runes: list[dict] = field(default_factory=list)

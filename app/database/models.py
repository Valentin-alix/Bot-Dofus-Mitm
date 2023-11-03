from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


# For hdv scrapping
class Object(Base):
    __tablename__ = "object"
    id: Mapped[int] = mapped_column(primary_key=True)
    object_gid: Mapped[int] = mapped_column(nullable=False)
    list_prices: Mapped[str] = mapped_column(nullable=False)


# For forgemagie
class Item(Base):
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    attempts: Mapped[int]

    def __repr__(self) -> str:
        return f"{self.name}"


class Rune(Base):
    __tablename__ = "rune"
    id: Mapped[int] = mapped_column(primary_key=True)
    rune_id: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[int] = mapped_column(nullable=False)
    reliquat_weight: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"


class TargetLine(Base):
    __tablename__ = "target_line"
    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[int] = mapped_column(nullable=False)
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id"), nullable=False)
    rune_id: Mapped[int] = mapped_column(ForeignKey("item.id"), nullable=False)
    line: Mapped[int] = mapped_column(nullable=False)
    column: Mapped[int] = mapped_column(nullable=False)

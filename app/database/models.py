from __future__ import annotations

import os
from datetime import datetime
from enum import Enum
from pathlib import Path
from pprint import pformat
from typing import List

from sqlalchemy import Column, ForeignKey, Table, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    def __str__(self) -> str:
        return pformat(vars(self))


class CategoryEnum(Enum):
    ALL = -1
    EQUIPMENT = 0
    CONSUMABLES = 1
    RESOURCES = 2
    QUEST = 3
    OTHER = 4
    COSMETICS = 5
    ECAFLIP_CARD = 238


sub_area_association = Table(
    "item_sub_area_association",
    Base.metadata,
    Column("item_id", ForeignKey("item.id")),
    Column("sub_area_id", ForeignKey("sub_area.id")),
)


class Item(Base):
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=False, comment="generic id"
    )
    name: Mapped[str] = mapped_column(nullable=False)
    type_item_id: Mapped[int] = mapped_column(
        ForeignKey("type_item.id"), nullable=False
    )
    level: Mapped[int] = mapped_column(nullable=False)
    weight: Mapped[int] = mapped_column(nullable=False)
    recycling_nuggets: Mapped[float] = mapped_column(nullable=False)
    favorite_recycling_sub_areas: Mapped[List[SubArea]] = relationship(
        secondary=sub_area_association
    )
    rune_id: Mapped[int] = mapped_column(ForeignKey("rune.id"), nullable=True)


class SubArea(Base):
    __tablename__ = "sub_area"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(nullable=False)


class TypeItem(Base):
    __tablename__ = "type_item"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(nullable=False)
    category: Mapped[CategoryEnum] = mapped_column(nullable=False)


class Recipe(Base):
    __tablename__ = "recipe"
    id: Mapped[int] = mapped_column(primary_key=True)
    result_item_id: Mapped[int] = mapped_column(
        ForeignKey("item.id"), nullable=False, unique=True
    )


class Ingredient(Base):
    __tablename__ = "ingredient"
    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipe.id"))


# For hdv scrapping
class Price(Base):
    __tablename__ = "price"
    id: Mapped[int] = mapped_column(primary_key=True)
    creation_date: Mapped[datetime] = mapped_column(nullable=False)
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id"), nullable=False)
    hundred: Mapped[int] = mapped_column(nullable=False)
    ten: Mapped[int] = mapped_column(nullable=False)
    one: Mapped[int] = mapped_column(nullable=False)
    server_id: Mapped[int] = mapped_column(nullable=False)


# For fm
class Rune(Base):
    __tablename__ = "rune"
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=False, comment="actionId"
    )
    weight: Mapped[float] = mapped_column(nullable=False)


def get_engine():
    return create_engine(
        f"sqlite:///{os.path.join(Path(__file__).parent, 'sqlite3.db')}",
        echo=False,
    )

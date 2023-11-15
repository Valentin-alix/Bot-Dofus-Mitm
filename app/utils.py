from typing import Type

import pandas as pd
from sqlalchemy import and_, func, desc, Engine
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy.orm.query import RowReturningQuery, Query

from app.database.models import Item, Price, TypeItem, CategoryEnum


def get_type(engine: Engine):
    with sessionmaker(bind=engine)() as session:
        types = session.query(TypeItem).order_by(TypeItem.name).distinct().all()
    return types


def get_items(engine: Engine) -> list[Type[Item]]:
    with sessionmaker(bind=engine)() as session:
        items = session.query(Item).order_by(Item.name).distinct().all()
    return items


def get_info_by_type_or_object(
        engine: Engine, type_name: str | None = None, object_name: str | None = None
) -> pd.DataFrame:
    with sessionmaker(bind=engine)() as session:
        if type_name is not None:
            filters = {and_(TypeItem.name == type_name)}
        else:
            filters = {and_(Item.name == object_name)}

        df_prices = pd.read_sql(
            session.query(Item, Price, TypeItem)
            .join(TypeItem, Item.type_item_id == TypeItem.id)
            .join(Price, Item.id == Price.item_id)
            .filter(*filters)
            .with_entities(
                Item.name, Price.creation_date, Price.one, Price.ten, Price.hundred
            )
            .statement,
            engine,
        )

    return df_prices


def get_difference_on_all_prices(
        engine: Engine, server_id: int, quantity: str = "ten", limit: int = 10
) -> RowReturningQuery[tuple[str, str, int]]:
    with sessionmaker(bind=engine)() as session:
        _items_latest_oldest_date = session.query(Item.id, func.max(Price.creation_date).label("max_date"),
                                                  func.min(Price.creation_date).label("min_date")).join(Price,
                                                                                                        Price.item_id == Item.id).group_by(
            Item.id).subquery()

        _items_latest = session.query(Item.id, Price.hundred).join(_items_latest_oldest_date,
                                                                   _items_latest_oldest_date.c.id == Item.id).join(
            Price, Price.item_id == Item.id).filter(
            Price.creation_date == _items_latest_oldest_date.c.max_date).group_by(
            Item.id).subquery()

        _items_oldest = session.query(Item.id, Price.hundred).join(_items_latest_oldest_date,
                                                                   _items_latest_oldest_date.c.id == Item.id).join(
            Price, Price.item_id == Item.id).filter(
            Price.creation_date == _items_latest_oldest_date.c.min_date).group_by(
            Item.id).subquery()

        difference_items = session.query(Price, TypeItem, Item).join(
            _items_latest,
            _items_latest.c.id == Price.item_id).join(
            _items_oldest,
            _items_oldest.c.id == Price.item_id).join(
            Item, Item.id == Price.item_id).join(TypeItem,
                                                 Item.type_item_id == TypeItem.id).filter(
            _items_latest.c.hundred != 0, _items_oldest.c.hundred != 0,
            TypeItem.category.in_([CategoryEnum.RESOURCES, CategoryEnum.CONSUMABLES]), Price.server_id == server_id
        ).group_by(Item.id).with_entities(TypeItem.name, Item.name,
                                          (_items_oldest.c.hundred - _items_latest.c.hundred).label(
                                              "benefit")).order_by(
            -(_items_oldest.c.hundred - _items_latest.c.hundred)).limit(
            limit)

    return difference_items


def get_benefit_nugget(engine: Engine, server_id: int, limit: int = 10) -> RowReturningQuery[
                                                                               tuple[str, list[
                                                                                   Item], int]] | Query | None:
    with sessionmaker(bind=engine)() as session:
        price_for_100_nugget = (
            session.query(Price.hundred)
            .filter(Price.server_id == server_id)
            .join(Item, Price.item_id == Item.id)
            .order_by(Price.creation_date)
            .filter(Item.name == "Pépite")
            .first()
        )
        if price_for_100_nugget is None:
            return None
        price_for_100_nugget = price_for_100_nugget[0]

        _items_latest = session.query(Item.id, func.max(Price.creation_date).label("max_date")).join(
            Price, Price.item_id == Item.id).group_by(
            Item.id).subquery()

        benefits_nugget = (
            session.query(
                Price,
                TypeItem.name,
                Item.name,
                func.round(
                    Item.recycling_nuggets * price_for_100_nugget - Price.hundred, 0
                ).label("benefits"),
                Item.favorite_recycling_sub_areas
            )
            .join(Item, Item.id == Price.item_id)
            .join(_items_latest, _items_latest.c.id == Item.id)
            .join(TypeItem, TypeItem.id == Item.type_item_id)
            .filter(Price.server_id == server_id, Price.creation_date == _items_latest.c.max_date)
            .group_by(Price.item_id)
            .having(Price.hundred != 0)
            .order_by(
                desc(Item.recycling_nuggets * price_for_100_nugget - Price.hundred)
            ).with_entities(TypeItem.name, Item, func.round(
                Item.recycling_nuggets * price_for_100_nugget - Price.hundred, 0
            ).label("benefits")).options(joinedload(Item.favorite_recycling_sub_areas))
            .limit(limit)
        )

    return benefits_nugget

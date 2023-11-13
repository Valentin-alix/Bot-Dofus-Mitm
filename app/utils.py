import pandas as pd
from sqlalchemy import Engine, and_, func, desc
from sqlalchemy.orm import sessionmaker, joinedload

from app.database.models import Item, Price, TypeItem, CategoryEnum


def get_type(engine: Engine):
    session = sessionmaker(bind=engine)()
    types = session.query(TypeItem).order_by(TypeItem.name).distinct().all()
    session.close()
    return types


def get_items(engine: Engine):
    session = sessionmaker(bind=engine)()
    items = session.query(Item).order_by(Item.name).distinct().all()
    session.close()
    return items


def get_info_by_type_or_object(
        engine: Engine, type_name: str | None = None, object_name: str | None = None
) -> pd.DataFrame:
    session = sessionmaker(bind=engine)()

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

    session.close()

    return df_prices


def get_difference_on_all_prices(engine: Engine, server_id: int, quantity: str = "ten",
                                 limit: int = 10) -> pd.DataFrame:
    session = sessionmaker(bind=engine)()

    df_prices = pd.read_sql(
        session.query(Item, Price, TypeItem)
        .join(Price, Item.id == Price.item_id)
        .join(TypeItem, Item.type_item_id == TypeItem.id)
        .filter(TypeItem.category == CategoryEnum.RESOURCES, Price.server_id == server_id)
        .statement,
        engine,
    )

    session.close()

    grouped = df_prices.groupby(by="name")[quantity].agg(["first", "last"])
    grouped = grouped[(grouped["first"] != 0) & (grouped["last"] != 0)][:limit]
    grouped["difference"] = grouped["last"] - grouped["first"]
    grouped["percentage_difference"] = grouped["difference"] / grouped["first"]

    result = grouped.sort_values(
        by="difference", ascending=True
    )
    return result


def get_benefit_nugget(engine: Engine, server_id: int, limit: int = 10):
    session = sessionmaker(bind=engine)()

    price_for_100_nugget = session.query(Price.hundred).filter(Price.server_id == server_id).join(Item,
                                                                                                  Price.item_id == Item.id).order_by(
        Price.creation_date).filter(
        Item.name == "Pépite").first()
    if price_for_100_nugget is None:
        return None

    benefits_nugget = session.query(
        Price, Item,
        func.max(Price.creation_date).label('maxdate'),
        func.round(Item.recycling_nuggets * price_for_100_nugget[0] - Price.hundred, 0).label("benefits")
    ).filter(Price.server_id == server_id).options(joinedload(Item.favorite_recycling_sub_areas)).join(Item,
                                                                                                       Item.id == Price.item_id).group_by(
        Price.item_id).having(Price.hundred != 0).order_by(
        desc(Item.recycling_nuggets * price_for_100_nugget[0] - Price.hundred)).limit(limit)

    return benefits_nugget

import pandas as pd
from sqlalchemy import and_, desc, func
from sqlalchemy.orm import Session, joinedload

from app.database.models import CategoryEnum, Ingredient, Item, Price, Recipe, TypeItem
from app.database.utils import ENGINE
from app.utils.debugger import timeit


@timeit
def get_types_items(session: Session):
    return session.query(TypeItem).order_by(TypeItem.name).distinct().all()


@timeit
def get_items(session: Session):
    return session.query(Item).order_by(Item.name).distinct().all()


@timeit
def get_recipes(session: Session):
    types_with_recipe = (
        session.query(Recipe)
        .join(Item, Item.id == Recipe.result_item_id)
        .join(TypeItem, TypeItem.id == Item.type_item_id)
        .with_entities(TypeItem)
        .order_by(TypeItem.name)
        .all()
    )
    return types_with_recipe


def get_benefit_from_craft(
    session: Session,
    server_id: int | None,
    category: CategoryEnum,
    type_name: str | None = None,
    limit=40,
):
    filters = [
        TypeItem.category == category,
    ]
    if type_name is not None:
        filters.append(TypeItem.name == type_name)

    _items_latest_date = (
        session.query(Price.item_id, func.max(Price.creation_date).label("latest_date"))
        .filter(Price.server_id == server_id)
        .group_by(Price.item_id)
        .subquery()
    )

    _price_latest_date = (
        session.query(Price.item_id, Price.one)
        .join(
            _items_latest_date,
            and_(
                _items_latest_date.c.item_id == Price.item_id,
                _items_latest_date.c.latest_date == Price.creation_date,
            ),
        )
        .subquery()
    )
    _recipes_info = (
        session.query(Recipe.id, Item.name, _price_latest_date.c.one)
        .join(
            _price_latest_date,
            _price_latest_date.c.item_id == Recipe.result_item_id,
        )
        .join(Item, Item.id == Recipe.result_item_id)
        .join(TypeItem, TypeItem.id == Item.type_item_id)
        .filter(*filters)
        .subquery()
    )

    _ingredients_info = (
        session.query(
            Ingredient.recipe_id,
            func.sum(_price_latest_date.c.one * Ingredient.quantity).label("cost"),
        )
        .join(_price_latest_date, _price_latest_date.c.item_id == Ingredient.item_id)
        .having(func.min(_price_latest_date.c.one) != 0)
        .group_by(Ingredient.recipe_id)
        .subquery()
    )

    return (
        session.query(Recipe.id)
        .join(_recipes_info, _recipes_info.c.id == Recipe.id)
        .join(_ingredients_info, _ingredients_info.c.recipe_id == Recipe.id)
        .order_by((_recipes_info.c.one - _ingredients_info.c.cost).desc())
        .with_entities(
            _recipes_info.c.name, _recipes_info.c.one - _ingredients_info.c.cost
        )
        .limit(limit)
        .all()
    )


@timeit
def get_benefit_nugget(
    session: Session, server_id: int | None, quantity: str, limit: int = 10
) -> list | None:
    if server_id is None:
        return None
    price_for_100_nugget = (
        session.query(getattr(Price, quantity))
        .filter(Price.server_id == server_id)
        .join(Item, Price.item_id == Item.id)
        .order_by(Price.creation_date.desc())
        .filter(Item.name == "Pépite")
        .first()
    )
    if price_for_100_nugget is None:
        return None

    price_for_100_nugget = price_for_100_nugget[0]

    _items_latest = (
        session.query(Item.id, func.max(Price.creation_date).label("max_date"))
        .join(Price, Price.item_id == Item.id)
        .filter(Price.server_id == server_id)
        .group_by(Item.id)
        .subquery()
    )

    benefits_nugget = (
        session.query(
            Price,
            TypeItem.name,
            Item.name,
            func.round(
                Item.recycling_nuggets * price_for_100_nugget
                - getattr(Price, quantity),
                0,
            ).label("benefits"),
            Item.favorite_recycling_sub_areas,
        )
        .join(Item, Item.id == Price.item_id)
        .join(_items_latest, _items_latest.c.id == Item.id)
        .join(TypeItem, TypeItem.id == Item.type_item_id)
        .filter(
            Price.server_id == server_id,
            Price.creation_date == _items_latest.c.max_date,
            TypeItem.category == CategoryEnum.RESOURCES,
        )
        .group_by(Price.item_id)
        .having(getattr(Price, quantity) != 0)
        .order_by(
            desc(
                Item.recycling_nuggets * price_for_100_nugget - getattr(Price, quantity)
            )
        )
        .with_entities(
            TypeItem.name,
            Item,
            func.round(
                Item.recycling_nuggets * price_for_100_nugget
                - getattr(Price, quantity),
                0,
            ).label("benefits"),
        )
        .options(joinedload(Item.favorite_recycling_sub_areas))
        .limit(limit)
        .all()
    )

    return benefits_nugget


@timeit
def get_info_by_type_or_object(
    session: Session, server_id: int | None, object_name: str | None = None
) -> pd.DataFrame | None:
    if server_id is None:
        return None
    # TODO Remove zeroes values
    df_prices = pd.read_sql(
        session.query(Item, Price, TypeItem)
        .join(TypeItem, Item.type_item_id == TypeItem.id)
        .join(Price, Item.id == Price.item_id)
        .filter(Item.name == object_name, Price.server_id == server_id)
        .with_entities(
            Item.name, Price.creation_date, Price.one, Price.ten, Price.hundred
        )
        .statement,
        ENGINE,
    )
    return df_prices


@timeit
def get_difference_on_all_prices(
    session: Session, server_id: int | None, quantity: str, limit: int = 10
) -> list | None:
    if server_id is None:
        print("server id is None")
        return None

    _items_latest_oldest_date = (
        session.query(
            Item.id,
            func.max(Price.creation_date).label("max_date"),
            func.min(Price.creation_date).label("min_date"),
        )
        .join(Price, Price.item_id == Item.id)
        .filter(Price.server_id == server_id)
        .group_by(Item.id)
        .subquery()
    )

    _items_latest = (
        session.query(Item.id, getattr(Price, quantity))
        .join(_items_latest_oldest_date, _items_latest_oldest_date.c.id == Item.id)
        .join(Price, Price.item_id == Item.id)
        .filter(Price.creation_date == _items_latest_oldest_date.c.max_date)
        .group_by(Item.id)
        .subquery()
    )

    _items_oldest = (
        session.query(Item.id, getattr(Price, quantity))
        .join(_items_latest_oldest_date, _items_latest_oldest_date.c.id == Item.id)
        .join(Price, Price.item_id == Item.id)
        .filter(Price.creation_date == _items_latest_oldest_date.c.min_date)
        .group_by(Item.id)
        .subquery()
    )

    difference_items = (
        session.query(TypeItem, Item)
        .join(_items_latest, _items_latest.c.id == Item.id)
        .join(_items_oldest, _items_oldest.c.id == Item.id)
        .join(TypeItem, Item.type_item_id == TypeItem.id)
        .filter(
            getattr(_items_latest.c, quantity) != 0,
            getattr(_items_oldest.c, quantity) != 0,
            TypeItem.category.in_([CategoryEnum.RESOURCES, CategoryEnum.CONSUMABLES]),
        )
        .group_by(Item.id)
        .with_entities(
            TypeItem.name,
            Item.name,
            (
                getattr(_items_oldest.c, quantity) - getattr(_items_latest.c, quantity)
            ).label("benefit"),
        )
        .order_by(
            -(getattr(_items_oldest.c, quantity) - getattr(_items_latest.c, quantity))
        )
        .limit(limit)
        .all()
    )

    return difference_items

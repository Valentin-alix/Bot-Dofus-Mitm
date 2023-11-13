import json
import os
from pathlib import Path

from sqlalchemy.orm import Session, sessionmaker
from tqdm import tqdm

from app.database.models import (
    CategoryEnum,
    Ingredient,
    Item,
    Recipe,
    SubArea,
    TypeItem,
    get_engine,
    Base, Rune,
)

BASE_PATH_OUTPUT = os.path.join(Path(__file__).parent.parent.parent, "resources")


def init_sub_areas(session: Session, d2i_texts: dict):
    d2o_sub_area_path = os.path.join(BASE_PATH_OUTPUT, "from_d2o", "SubAreas.json")
    print("importing sub areas")
    with open(d2o_sub_area_path, encoding="utf8") as sub_areas_file:
        sub_areas = json.load(sub_areas_file)
        sub_areas_entities = []
        for sub_area in tqdm(sub_areas):
            if session.query(SubArea).get(sub_area["id"]) is None:
                sub_areas_entities.append(
                    SubArea(
                        id=sub_area["id"], name=d2i_texts.get(str(sub_area["nameId"]))
                    )
                )
        session.add_all(sub_areas_entities)
        session.flush()


def init_type(session: Session, d2i_texts: dict):
    d2o_type_path = os.path.join(BASE_PATH_OUTPUT, "from_d2o", "ItemTypes.json")
    print("importing types")
    with open(d2o_type_path, encoding="utf8") as d2o_type_file:
        type_items = json.load(d2o_type_file)
        type_items_entities = []
        for _type in tqdm(type_items):
            if session.query(TypeItem).get(_type["id"]) is None:
                type_items_entities.append(
                    TypeItem(
                        id=_type["id"],
                        name=d2i_texts.get(str(_type["nameId"])),
                        category=CategoryEnum(_type["categoryId"]),
                    )
                )
        session.add_all(type_items_entities)
        session.flush()


def init_item(session: Session, d2i_texts: dict):
    d2o_item_path = os.path.join(BASE_PATH_OUTPUT, "from_d2o", "Items.json")
    print("importing item")
    with open(d2o_item_path, encoding="utf8") as d2o_item_file:
        items = json.load(d2o_item_file)
        items_entities = []
        for item in tqdm(items):
            if (
                    item["isSaleable"] is True
                    and session.query(Item).get(item["id"]) is None
            ):
                item_object = Item(
                    id=item["id"],
                    name=d2i_texts.get(str(item["nameId"])),
                    type_item_id=item["typeId"],
                    level=item["level"],
                    weight=item["realWeight"],
                    recycling_nuggets=item["recyclingNuggets"],
                )
                item_object.favorite_recycling_sub_areas.extend(
                    session.query(SubArea).filter(
                        SubArea.id.in_(item["favoriteRecyclingSubareas"])
                    )
                )
                items_entities.append(item_object)
        session.add_all(items_entities)
        session.flush()


def init_recipes(session: Session):
    d2o_recipe_path = os.path.join(BASE_PATH_OUTPUT, "from_d2o", "Recipes.json")
    print("importing recipes")
    with open(d2o_recipe_path, encoding="utf8") as d2o_recipe_file:
        recipes = json.load(d2o_recipe_file)
        recipes_entites = []
        ingredients_entites = []
        for recipe in tqdm(recipes):
            if (
                    session.query(Recipe.id)
                            .filter_by(result_item_id=recipe["resultId"])
                            .first()
                    is None
            ):
                recipe_object = Recipe(result_item_id=recipe["resultId"])
                session.add(recipe_object)
                session.flush()
                ingredients_entites.extend(
                    Ingredient(
                        item_id=ingredient[0],
                        quantity=ingredient[1],
                        recipe_id=recipe_object.id,
                    )
                    for ingredient in zip(recipe["ingredientIds"], recipe["quantities"])
                )
                recipes_entites.append(Recipe(result_item_id=recipe["resultId"]))

        session.add_all(ingredients_entites)
        session.flush()


def maj_runes_objects(session: Session):
    with open(os.path.join(Path(__file__).parent.parent.parent, "resources", "runes.json")) as rune_file:
        runes = json.load(rune_file)
        runes_entities = []
        for rune in runes:
            if session.query(Rune).filter_by(id=rune["positive_effect_Id"]).first() is None:
                positive_rune = Rune(id=rune["positive_effect_Id"], weight=rune["weight"])
                runes_entities.append(positive_rune)
                session.flush()
                session.query(Item).filter(Item.id.in_(_item["id"] for _item in rune['runes'])).update(
                    {Item.rune_id: positive_rune.id})

            if (negative_rune_id := rune.get("negative_effect_Id", None)) is not None and session.query(Rune).filter_by(
                    id=negative_rune_id).first() is None:
                runes_entities.append(Rune(id=negative_rune_id, weight=rune["weight"] / 2))

    session.add_all(runes_entities)
    session.flush()


def init_bdd():
    engine = get_engine()
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    d2i_path = os.path.join(BASE_PATH_OUTPUT, "from_d2i.json")
    with open(d2i_path, encoding="utf8") as d2i_file:
        d2i_texts = json.load(d2i_file)["texts"]
        init_sub_areas(session, d2i_texts)
        init_type(session, d2i_texts)
        init_item(session, d2i_texts)
        init_recipes(session)
        maj_runes_objects(session)

    session.commit()
    session.close()

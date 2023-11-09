import json
import os
from pathlib import Path
from sqlalchemy.orm import Session, sessionmaker
from tqdm import tqdm


from database.models import (
    CategoryEnum,
    Ingredient,
    Item,
    Recipe,
    SubArea,
    TypeItem,
    get_engine,
    Base,
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

    session.commit()
    session.close()


# def maj_runes_objects(engine: Engine):
#     list_rune: Dict[int, str] = {
#         111: "PA",
#         112: "Dommages",
#         115: "%Critique",
#         117: "Portée",
#         118: "Force",
#         119: "Agilité",
#         123: "Chance",
#         124: "Sagesse",
#         125: "Vitalité",
#         126: "Intelligence",
#         128: "PM",
#         138: "Puissance",
#         158: "Pods",
#         160: "EsquivePA",
#         161: "EsquivePM",
#         174: "Initiative",
#         176: "Prospection",
#         178: "Soins",
#         182: "Invocations",
#         210: "%RésistanceTerre",
#         211: "%RésistanceEau",
#         212: "%RésistanceAir",
#         213: "%RésistanceFeu",
#         214: "%RésistanceNeutre",
#         220: "Renvoiedommages",
#         225: "DommagesPièges",
#         226: "Puissance(pièges)",
#         240: "RésistanceTerre",
#         241: "RésistanceEau",
#         242: "RésistanceAir",
#         243: "RésistanceFeu",
#         244: "RésistanceNeutre",
#         410: "RetraitPA",
#         412: "RetraitPM",
#         414: "DommagesPoussée",
#         416: "RésistancePoussée",
#         418: "DommagesCritiques",
#         420: "RésistanceCritiques",
#         422: "DommagesTerre",
#         424: "DommagesFeu",
#         426: "DommagesEau",
#         428: "DommagesAir",
#         430: "DommagesNeutre",
#         752: "Fuite",
#         753: "Tacle",
#         795: "Armedechasse",
#         2800: "%Dommagesmêlée",
#         2803: "%Résistancemêlée",
#         2804: "%Dommagesdistance",
#         2807: "%Résistancedistance",
#         2808: "%Dommagesd'armes",
#         2812: "%Dommagesauxsorts",
#     }
#     session = sessionmaker(bind=engine)()

#     session.query(Rune).delete()
#     session.commit()

#     runes: List[Rune] = []
#     for key, value in list_rune.items():
#         runes.append(Rune(rune_id=key, name=value))

#     session.add_all(runes)
#     session.commit()
#     session.close()

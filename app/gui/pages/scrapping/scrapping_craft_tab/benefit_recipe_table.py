from PyQt5.QtWidgets import QLabel, QTableWidgetItem
from sqlalchemy import Engine, func, and_
from sqlalchemy.orm import sessionmaker

from app.database.models import CategoryEnum, Item, Price, Ingredient, Recipe, TypeItem
from app.gui.components.common import Widget, TableWidget
from app.gui.components.organization import VerticalLayout


class BenefitRecipeTable(Widget):
    def __init__(self, engine: Engine):
        super().__init__()
        self.engine = engine
        self.server_id: int | None
        v_layout = VerticalLayout()
        self.setLayout(v_layout)

        title = QLabel(parent=self, text="Meilleur bénéfice sur les crafts")
        v_layout.addWidget(title)

        table_benefit_recipe_scroll = TableWidget(["Nom", "Bénéfice"])
        self.table_benefit_recipe = table_benefit_recipe_scroll.table
        v_layout.addWidget(table_benefit_recipe_scroll)

    def get_benefit_recipe(self, category: CategoryEnum, type_name: str | None = None):
        self.table_benefit_recipe.clearContents()
        self.table_benefit_recipe.setRowCount(0)

        rows = 40

        benefit_recipe = get_benefit_from_craft(self.engine, self.server_id, category, type_name, rows)

        self.table_benefit_recipe.setRowCount(benefit_recipe.count())
        for index, (name, benefit) in enumerate(benefit_recipe):
            name_col = QTableWidgetItem(name)
            benefit_col = QTableWidgetItem(str(benefit))

            self.table_benefit_recipe.setItem(index, 0, name_col)
            self.table_benefit_recipe.setItem(index, 1, benefit_col)


def get_benefit_from_craft(engine: Engine, server_id: int | None, category: CategoryEnum,
                           type_name: str | None = None, limit=40):
    with sessionmaker(bind=engine)() as session:
        filters = [
            TypeItem.category == category,
        ]
        if type_name is not None:
            filters.append(TypeItem.name == type_name)

        _items_latest_date = (
            session.query(
                Price.item_id,
                func.max(Price.creation_date).label("latest_date")
            )
            .filter(Price.server_id == server_id)
            .group_by(Price.item_id)
            .subquery()
        )

        _price_latest_date = (
            session.query(
                Price.item_id,
                Price.one
            ).join(
                _items_latest_date, and_(
                    _items_latest_date.c.item_id == Price.item_id,
                    _items_latest_date.c.latest_date == Price.creation_date)
            )
            .subquery()
        )
        _recipes_info = (session.query(Recipe.id, Item.name, _price_latest_date.c.one)
                         .join(_price_latest_date,
                               _price_latest_date.c.item_id == Recipe.result_item_id)
                         .join(Item, Item.id == Recipe.result_item_id)
                         .join(TypeItem, TypeItem.id == Item.type_item_id)
                         .filter(*filters)
                         .subquery()
                         )

        _ingredients_info = (
            session.query(Ingredient.recipe_id, func.sum(_price_latest_date.c.one * Ingredient.quantity).label('cost'))
            .join(_price_latest_date, _price_latest_date.c.item_id == Ingredient.item_id)
            .having(func.min(_price_latest_date.c.one) != 0)
            .group_by(Ingredient.recipe_id).subquery())

        return (session.query(Recipe.id)
                .join(_recipes_info, _recipes_info.c.id == Recipe.id)
                .join(_ingredients_info, _ingredients_info.c.recipe_id == Recipe.id)
                .order_by((_recipes_info.c.one - _ingredients_info.c.cost).desc())
                .with_entities(_recipes_info.c.name, _recipes_info.c.one - _ingredients_info.c.cost)
                .limit(limit))

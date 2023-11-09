import pandas as pd

import matplotlib.pyplot as plt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from database.models import Object, Price, TypeObject, get_engine

SERVER_ID = 291


class Analaysis:
    def __init__(self) -> None:
        self.engine = get_engine()

    def get_infos_by_type_or_object(
        self, type_name: str | None = None, object_name: str | None = None
    ) -> pd.DataFrame:
        session = sessionmaker(bind=self.engine)()

        filters = {}

        if type_name is not None:
            filters = {and_(TypeObject.name == type_name)}
        else:
            filters = {and_(Object.name == object_name)}

        df_prices = pd.read_sql(
            session.query(Object, Price, TypeObject)
            .join(TypeObject, Object.type_object_id == TypeObject.id)
            .join(Price, Object.id == Price.object_id)
            .filter(*filters)
            .with_entities(Object.name, Price.creation_date, Price.list_prices)
            .statement,
            self.engine,
        )

        session.close()

        if len(df_prices) > 0:
            df_prices[["1", "10", "100"]] = (
                df_prices["list_prices"]
                .str.split(",")
                .apply(lambda x: pd.Series([int(val) for val in x]))
            )
            df_prices.pop("list_prices")

        return df_prices

    def get_difference_on_all_prices(self, quantity: int = 1) -> pd.DataFrame:
        session = sessionmaker(bind=self.engine)()

        df_prices = pd.read_sql(
            session.query(Object, Price, TypeObject)
            .join(TypeObject, Object.type_object_id == TypeObject.id)
            .join(Price, Object.id == Price.object_id)
            .with_entities(Object.name, Price.creation_date, Price.list_prices)
            .statement,
            self.engine,
        )

        session.close()

        if len(df_prices) > 0:
            df_prices[["1", "10", "100"]] = (
                df_prices["list_prices"]
                .str.split(",")
                .apply(lambda x: pd.Series([int(val) for val in x]))
            )
            df_prices.pop("list_prices")

        grouped = df_prices.groupby(by="name")[str(quantity)].agg(["first", "last"])
        grouped = grouped[(grouped["first"] != 0) & (grouped["last"] != 0)]
        grouped["difference"] = grouped["last"] - grouped["first"]
        grouped["percentage_difference"] = grouped["difference"] / grouped["first"]

        result = grouped[grouped["percentage_difference"] < -0.3].sort_values(
            by="percentage_difference", ascending=True
        )

        return result

    def generate_graph_by_quantity(self, df_infos: pd.DataFrame) -> None:
        plt.figure(figsize=(10, 8))
        plt.xlabel("Date de création")
        plt.ylabel(f"Prix par 1, 10 et 100")

        for name in df_infos["name"]:
            df_filtered = df_infos[df_infos["name"] == name]
            plt.plot(df_filtered["creation_date"], df_filtered[str(100)], label=name)
            plt.plot(df_filtered["creation_date"], df_filtered[str(10)], label=name)
            plt.plot(df_filtered["creation_date"], df_filtered[str(1)], label=name)

        plt.show()


if __name__ == "__main__":
    anal = Analaysis()
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)

    print(anal.get_difference_on_all_prices(10))
    df = anal.get_infos_by_type_or_object(object_name="Rune Vi")
    anal.generate_graph_by_quantity(df)

import pandas as pd

import matplotlib.pyplot as plt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from database.models import Object, Price, TypeObject, get_engine


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

        prices_potion_df = pd.read_sql(
            session.query(Object, Price, TypeObject)
            .join(TypeObject, Object.type_object_id == TypeObject.id)
            .join(Price, Object.id == Price.object_id)
            .filter(*filters)
            .with_entities(Object.name, Price.creation_date, Price.list_prices)
            .statement,
            self.engine,
        )

        session.close()

        if len(prices_potion_df) > 0:
            prices_potion_df[["1", "10", "100"]] = (
                prices_potion_df["list_prices"]
                .str.split(",")
                .apply(lambda x: pd.Series([int(val) for val in x]))
            )
            prices_potion_df.pop("list_prices")

        return prices_potion_df

    def generate_graph_by_quantity(
        self, df_infos: pd.DataFrame, quantity: int = 100
    ) -> None:
        plt.figure(figsize=(10, 8))
        plt.xlabel("Date de création")
        plt.ylabel(f"Prix par {quantity}")

        for name in df_infos["name"]:
            df_filtered = df_infos[df_infos["name"] == name]
            plt.plot(
                df_filtered["creation_date"], df_filtered[str(quantity)], label=name
            )

        plt.legend()
        plt.show()


if __name__ == "__main__":
    anal = Analaysis()
    df = anal.get_infos_by_type_or_object(type_name="Bois")
    anal.generate_graph_by_quantity(df)

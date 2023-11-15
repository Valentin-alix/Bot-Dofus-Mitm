from __future__ import annotations

import os
import sys

from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.database.models import get_engine, Item, SubArea

if __name__ == "__main__":
    engine = get_engine()

    session = sessionmaker(engine)()

    print(
        session.query(SubArea.name)
        .join(Item.favorite_recycling_sub_areas)
        .filter(Item.name == "Sachet d'Oignons")
        .all()
    )

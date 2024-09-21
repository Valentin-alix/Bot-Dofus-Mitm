import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine():
    return create_engine(
        f"sqlite:///{os.path.join(Path(__file__).parent, 'sqlite3.db')}",
        echo=False,
    )


ENGINE = get_engine()


SessionLocal = sessionmaker(bind=ENGINE)

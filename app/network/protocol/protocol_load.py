import pickle
from pathlib import Path

with (Path(__file__).parent / "protocol.pk").open("rb") as file:
    types = pickle.load(file)
    msg_from_id = pickle.load(file)
    types_from_id = pickle.load(file)
    primitives = pickle.load(file)

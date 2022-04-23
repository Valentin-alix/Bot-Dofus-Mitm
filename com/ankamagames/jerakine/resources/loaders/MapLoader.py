from functools import lru_cache
from pathlib import Path
from com.ankamagames.dofus import Constants
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from dataAdapter.dlm import DLM


class MapLoader(metaclass=Singleton):
    DLM_KEY = "649ae451ca33ec53bbcbcc33becf15f4"

    def __init__(self) -> None:
        self._reader = DLM(self.DLM_KEY)

    @lru_cache(maxsize=256)
    def load(self, mapId, key=None):
        if key is not None:
            self._reader.setKey(key)
        map_p = Path(Constants.MAPS_PATH) / MapLoader.getMapURI(mapId)
        if not map_p.exists():
            raise Exception(f"Map {mapId} not found in path {map_p}")
        with open(map_p, "rb") as f:
            compressedMapBinary = f.read()
            return self._reader.read(compressedMapBinary)

    def getMapURI(mapId):
        return f"{int(mapId) % 10}/{int(mapId)}.dlm"

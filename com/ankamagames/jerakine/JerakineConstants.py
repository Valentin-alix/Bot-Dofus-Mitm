from com.ankamagames.jerakine.types.DataStoreType import DataStoreType
from com.ankamagames.jerakine.types.enums.DataStoreEnum import DataStoreEnum


LOADERS_POOL_INITIAL_SIZE: int = 5

LOADERS_POOL_GROW_SIZE: int = 5

LOADERS_POOL_WARN_LIMIT: int = 80

URLLOADERS_POOL_INITIAL_SIZE: int = 3

URLLOADERS_POOL_GROW_SIZE: int = 2

URLLOADERS_POOL_WARN_LIMIT: int = 10

RECTANGLE_POOL_INITIAL_SIZE: int = 5

RECTANGLE_POOL_GROW_SIZE: int = 50

RECTANGLE_POOL_WARN_LIMIT: int = 1000

POINT_POOL_INITIAL_SIZE: int = 50

POINT_POOL_GROW_SIZE: int = 50

POINT_POOL_WARN_LIMIT: int = 1000

SOUND_POOL_INITIAL_SIZE: int = 5

SOUND_POOL_GROW_SIZE: int = 50

SOUND_POOL_WARN_LIMIT: int = 1000

LINKED_LIST_NODE_POOL_INITIAL_SIZE: int = 100

LINKED_LIST_NODE_POOL_GROW_SIZE: int = 50

LINKED_LIST_NODE_POOL_WARN_LIMIT: int = 1000

TEXTURES_CACHE_SIZE: int = 25

XML_CACHE_SIZE: int = 10

MOBILES_CACHE_SIZE: int = 10

MAX_PARALLEL_LOADINGS: int = 6

DATASTORE_CLASS_ALIAS: DataStoreType = DataStoreType(
    "Jerakine_classAlias",
    True,
    DataStoreEnum.LOCATION_LOCAL,
    DataStoreEnum.BIND_COMPUTER,
)

DATASTORE_LANG: DataStoreType = DataStoreType(
    "Jerakine_lang", True, DataStoreEnum.LOCATION_LOCAL, DataStoreEnum.BIND_COMPUTER
)

DATASTORE_LANG_VERSIONS: DataStoreType = DataStoreType(
    "Jerakine_lang_vesrion",
    True,
    DataStoreEnum.LOCATION_LOCAL,
    DataStoreEnum.BIND_COMPUTER,
)

DATASTORE_FILES_INFO: DataStoreType = DataStoreType(
    "Jerakine_file_version",
    True,
    DataStoreEnum.LOCATION_LOCAL,
    DataStoreEnum.BIND_COMPUTER,
)

DATASTORE_MD5: DataStoreType = DataStoreType(
    "Jerakine_md5", True, DataStoreEnum.LOCATION_LOCAL, DataStoreEnum.BIND_COMPUTER
)

DATASTORE_GAME_DATA: DataStoreType = DataStoreType(
    "Jerakine_gameData", True, DataStoreEnum.LOCATION_LOCAL, DataStoreEnum.BIND_COMPUTER
)

WORLD_ENTITY_POOL_INITIAL_SIZE: int = 40

WORLD_ENTITY_POOL_GROW_SIZE: int = 10

WORLD_ENTITY_POOL_WARN_LIMIT: int = 100

JSON_ENCODER_POOL_INITIAL_SIZE: int = 5

JSON_ENCODER_POOL_GROW_SIZE: int = 5

JSON_ENCODER_POOL_WARN_LIMIT: int = 80

JSON_DECODER_POOL_INITIAL_SIZE: int = 5

JSON_DECODER_POOL_GROW_SIZE: int = 5

JSON_DECODER_POOL_WARN_LIMIT: int = 80

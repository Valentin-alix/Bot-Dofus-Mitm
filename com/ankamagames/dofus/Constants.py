# SIGNATURE_KEY_DATA = Constants_SIGNATURE_KEY_DATA

import os
from pathlib import Path
from com.ankamagames.jerakine.types.DataStoreType import DataStoreType
from com.ankamagames.jerakine.types.enums.DataStoreEnum import DataStoreEnum


LOG_UPLOAD_MODE = False

EVENT_MODE = False

EVENT_MODE_PARAM = ""

CHARACTER_CREATION_ALLOWED = True

PRE_GAME_MODULE = ["Ankama_Connection"]

COMMON_GAME_MODULE = [
    "Ankama_Common",
    "Ankama_Config",
    "Ankama_Tooltips",
    "Ankama_Console",
    "Ankama_ContextMenu",
]

ADMIN_MODULE = ["Ankama_Admin"]

DETERMINIST_TACKLE = True

DATASTORE_MODULE_DEBUG: DataStoreType = DataStoreType(
    "Dofus_ModuleDebug", True, DataStoreEnum.LOCATION_LOCAL, DataStoreEnum.BIND_COMPUTER
)

DATASTORE_COMPUTER_OPTIONS: DataStoreType = DataStoreType(
    "Dofus_ComputerOptions",
    True,
    DataStoreEnum.LOCATION_LOCAL,
    DataStoreEnum.BIND_ACCOUNT,
)

MAX_LOGIN_ATTEMPTS = 3

ROOTDIR = Path(os.path.dirname(__file__))

MAPS_PATH = Path("content/maps")

DOFUS_ROOTDIR = Path(os.getenv("LOCALAPPDATA")) / "Ankama" / "Dofus"

DOFUS_DATA_DIR = DOFUS_ROOTDIR / "data"

DOFUS_COMMON_DIR = DOFUS_DATA_DIR / "common"

DOFUS_LOCAL_DATA_STORE = Path(os.getenv("APPDATA")) / "Dofus"

DOFUS_CONTENT_DIR = DOFUS_ROOTDIR / "content"

PROTOCOL_SPEC_PATH = (
    ROOTDIR / ".." / "jerakine" / "network" / "parser" / "D2protocol.json"
)

WORLDGRAPH_PATH = DOFUS_CONTENT_DIR / "maps" / "world-graph.binary"

LANG_FILE_PATH = DOFUS_DATA_DIR / "i18n" / "i18n_fr.d2i"

PROTOCOL_MSG_SHUFFLE_PATH = ROOTDIR / "network" / "MsgShuffle.json"

GAME_VERSION_PATH = DOFUS_ROOTDIR / "VERSION"

BINARY_DATA_DIR = ROOTDIR / "../../../binaryData"

import json
from pathlib import Path
from typing import List, Dict
import os
import shutil
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
from sqlalchemy import Engine, exists
from PyDofus.d2i_unpack import d2i_unpack
from PyDofus.d2o_unpack import d2o_unpack

from database.models import Object, Rune


def maj_runes_objects(engine: Engine):
    list_rune: Dict[int, str] = {
        111: "PA",
        112: "Dommages",
        115: "%Critique",
        117: "Portée",
        118: "Force",
        119: "Agilité",
        123: "Chance",
        124: "Sagesse",
        125: "Vitalité",
        126: "Intelligence",
        128: "PM",
        138: "Puissance",
        158: "Pods",
        160: "EsquivePA",
        161: "EsquivePM",
        174: "Initiative",
        176: "Prospection",
        178: "Soins",
        182: "Invocations",
        210: "%RésistanceTerre",
        211: "%RésistanceEau",
        212: "%RésistanceAir",
        213: "%RésistanceFeu",
        214: "%RésistanceNeutre",
        220: "Renvoiedommages",
        225: "DommagesPièges",
        226: "Puissance(pièges)",
        240: "RésistanceTerre",
        241: "RésistanceEau",
        242: "RésistanceAir",
        243: "RésistanceFeu",
        244: "RésistanceNeutre",
        410: "RetraitPA",
        412: "RetraitPM",
        414: "DommagesPoussée",
        416: "RésistancePoussée",
        418: "DommagesCritiques",
        420: "RésistanceCritiques",
        422: "DommagesTerre",
        424: "DommagesFeu",
        426: "DommagesEau",
        428: "DommagesAir",
        430: "DommagesNeutre",
        752: "Fuite",
        753: "Tacle",
        795: "Armedechasse",
        2800: "%Dommagesmêlée",
        2803: "%Résistancemêlée",
        2804: "%Dommagesdistance",
        2807: "%Résistancedistance",
        2808: "%Dommagesd'armes",
        2812: "%Dommagesauxsorts",
    }
    session = sessionmaker(bind=engine)()

    session.query(Rune).delete()
    session.commit()

    runes: List[Rune] = []
    for key, value in list_rune.items():
        runes.append(Rune(rune_id=key, name=value))

    session.add_all(runes)
    session.commit()
    session.close()


def get_as_scripts(output_as_scripts: str):
    selected_classes = "com.ankamagames.dofus.BuildInfos,com.ankamagames.dofus.network.++,com.ankamagames.jerakine.network.++"
    if os.path.exists(output_as_scripts):
        shutil.rmtree(output_as_scripts)
    os.system(
        f'java -Xmx10512m  -jar "{os.environ.get("FFDECJAR_PATH")}"\
        -config=parallelSpeedUp=0 -selectclass={selected_classes}\
        -export script "{output_as_scripts}" "{os.environ.get("DOFUS_INVOKER")}"'
    )


def update_resources(engine: Engine):
    load_dotenv()

    if (
        (dofus_invoker_path := os.environ.get("DOFUS_INVOKER", None)) is not None
        and os.environ.get("FFDECJAR_PATH", None) is not None
        and os.environ.get("D2O_FOLDER", None) is not None
        and os.environ.get("D2I_FILE") is not None
    ):
        output_as_scripts = os.path.join(Path(__file__).parent.parent, "as_scripts")
        if os.path.getmtime(output_as_scripts) <= os.path.getmtime(dofus_invoker_path):
            get_as_scripts(output_as_scripts)

            # Building protocol pk to parse message network
            os.system("python app/network/protocol/build_protocol.py")

            d2o_unpack(os.environ.get("D2O_FOLDER"))
            d2i_unpack(os.environ.get("D2I_FILE"))

            init_objects(engine)

        # maj_runes_objects(engine)
    else:
        raise KeyError(".env file not valid")


def init_objects(engine: Engine):
    session = sessionmaker(bind=engine)()

    d2o_item_file_path = os.path.join(
        Path(__file__).parent, "PyDofus", "output", "d2o", "Items.json"
    )
    d2i_file_path = os.path.join(
        Path(__file__).parent, "PyDofus", "output", "i18n_fr.json"
    )

    with open(d2o_item_file_path, encoding="utf8") as d2o_file, open(
        d2i_file_path, encoding="utf8"
    ) as d2i_file:
        d2o_items = json.load(d2o_file)
        d2i_texts = json.load(d2i_file)["texts"]

        objects = (
            Object(object_gid=object_gid, name=name)
            for d2o_item in d2o_items
            if (object_gid := d2o_item.get("id", None)) is not None
            and (name := d2i_texts.get(str(d2o_item.get("nameId")), None)) is not None
            and not session.query(
                exists().where(Object.object_gid == object_gid or Object.name == name)
            ).scalar()
        )
        session.add_all(objects)

        session.commit()
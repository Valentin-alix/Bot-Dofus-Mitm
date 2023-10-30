import json
import os
import re
import shutil

from dotenv import load_dotenv
from PyDofus.pydofus.d2o import D2OReader, InvalidD2OFile

from app.database import execute_sql, get_connection


def maj_runes_objects():
    list_rune = {
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
    execute_sql("delete from rune")
    for key, value in list_rune.items():
        execute_sql("insert into rune(rune_id, rune_name) values (?, ?)", (key, value))


def get_as_scripts(output_as_scripts):
    if os.path.exists(output_as_scripts):
        shutil.rmtree(output_as_scripts)
    os.system(
        f'java -Xmx10512m  -jar  "{os.environ.get("FFDECJAR_PATH")}" -export script "{output_as_scripts}" "{os.environ.get("DOFUS_INVOKER")}"'
    )


def get_d2o_json(output_d2o_json):
    if os.path.exists(output_d2o_json):
        shutil.rmtree(output_d2o_json)
    os.mkdir(output_d2o_json)
    for file_ in os.listdir(os.environ.get("D2O_FOLDER")):
        if file_.endswith(".d2o"):
            file_name = os.path.basename(file_)
            d2p_file = open(os.path.join(os.environ.get("D2O_FOLDER"), file_), "rb")

            print("D2O Unpacker for " + file_name)

            try:
                d2o_reader = D2OReader(d2p_file)
                d2o_data = d2o_reader.get_objects()

                json_output = open(
                    os.path.join(output_d2o_json, file_name.replace("d2o", "json")),
                    "w",
                )
                json.dump(d2o_data, json_output, indent=4)
                json_output.close()
            except InvalidD2OFile:
                pass


if __name__ == "__main__":
    load_dotenv()

    # Creating database structure
    if not os.path.exists("sqlite3.db"):
        cursor = get_connection().cursor()
        with open("tables.sql") as file:
            cursor.executescript(file.read())

    OUTPUT_AS_SCRIPTS = "as_scripts"
    if os.path.getmtime(OUTPUT_AS_SCRIPTS) <= os.path.getmtime(
        os.environ.get("DOFUS_INVOKER")
    ):
        get_as_scripts(OUTPUT_AS_SCRIPTS)

        # Building protocol pk to parse message network
        os.system("python app/network/protocol/build_protocol.py")

    OUTPUT_D2O_JSON = "d2o_json"
    if os.path.getmtime(OUTPUT_D2O_JSON) <= os.path.getmtime(
        os.environ.get("D2O_FOLDER")
    ):
        get_d2o_json(OUTPUT_D2O_JSON)

    # TODO Exploit D2O_JSON
    maj_runes_objects()

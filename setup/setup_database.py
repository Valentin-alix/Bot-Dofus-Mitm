import re
from os import walk

from databases.database import Database


def setup_list_runes(db: Database):
    list_rune = {111: "PA", 112: "Dommages", 115: "%Critique", 117: "Portée", 118: "Force", 119: "Agilité",
                 123: "Chance",
                 124: "Sagesse", 125: "Vitalité", 126: "Intelligence", 128: "PM", 138: "Puissance", 158: "Pods",
                 160: "EsquivePA", 161: "EsquivePM", 174: "Initiative", 176: "Prospection", 178: "Soins",
                 182: "Invocations", 210: "%RésistanceTerre", 211: "%RésistanceEau", 212: "%RésistanceAir",
                 213: "%RésistanceFeu", 214: "%RésistanceNeutre", 220: "Renvoiedommages", 225: "DommagesPièges",
                 226: "Puissance(pièges)", 240: "RésistanceTerre", 241: "RésistanceEau", 242: "RésistanceAir",
                 243: "RésistanceFeu", 244: "RésistanceNeutre", 410: "RetraitPA", 412: "RetraitPM",
                 414: "DommagesPoussée",
                 416: "RésistancePoussée", 418: "DommagesCritiques", 420: "RésistanceCritiques", 422: "DommagesTerre",
                 424: "DommagesFeu", 426: "DommagesEau", 428: "DommagesAir", 430: "DommagesNeutre", 752: "Fuite",
                 753: "Tacle", 795: "Armedechasse", 2800: "%Dommagesmêlée", 2803: "%Résistancemêlée",
                 2804: "%Dommagesdistance", 2807: "%Résistancedistance", 2808: "%Dommagesd'armes",
                 2812: "%Dommagesauxsorts"}
    db.delete_all_rune()
    for cle, valeur in list_rune.items():
        db.insert_rune(cle, valeur)


def maj_protocol_id(db: Database):
    db.delete_message_network()
    for (repertoire, sousRepertoires, fichiers) in walk("as_script_resources"):
        for file in fichiers:
            with open(repertoire + "\\" + file) as opened_file:
                lines = opened_file.readlines()
                [db.insert_message_network(re.findall(r'\d+', line)[0], file[:-3]) for line in lines if
                 "protocolId:uint" in line]


if __name__ == "__main__":
    database = Database()
    maj_protocol_id(database)
    # setup_list_runes(database)

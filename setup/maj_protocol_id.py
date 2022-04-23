from os import walk
import re

import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bot_sniffer",
)

with database.cursor() as request:
    request.execute("delete from message_network")
    for (repertoire, sousRepertoires, fichiers) in walk("./static/scripts_resources"):
        for file in fichiers:
            with open(repertoire + "\\" + file) as opened_file:
                lines = opened_file.readlines()
                for line in lines:
                    if "protocolId:uint" in line:
                        request.execute("insert into message_network(id_message, name_message) values (%s, %s)",
                                        (re.findall(r'\d+', line)[0], file[:-3]))
                        database.commit()
                        break

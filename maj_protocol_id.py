from os import walk
import re

import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bot_sniffer",
)


def insert_id_in_white_list():
    with database.cursor() as request:
        request.execute("delete from white_list")
        for (repertoire, sousRepertoires, fichiers) in walk("decompiled_scripts"):
            for file in fichiers:
                with open(repertoire + "\\" + file) as opened_file:
                    lines = opened_file.readlines()
                    for line in lines:
                        if "protocolId:uint" in line:
                            request.execute("insert into white_list(white_list_id) values (%s)",
                                            (re.findall(r'\d+', line)[0],))
                            database.commit()


def update_fm_and_item_id():
    with database.cursor() as request:
        request.execute("delete from message_network")
        for (repertoire, sousRepertoires, fichiers) in walk("decompiled_scripts"):
            for file in fichiers:
                with open(repertoire + "\\" + file) as opened_file:
                    lines = opened_file.readlines()
                    for line in lines:
                        if file == "ExchangeCraftResultMagicWithObjectDescMessage.as" or file == "ExchangeObjectAddedMessage.as":
                            if "protocolId:uint" in line:
                                request.execute("insert into message_network(id_message, name_message) values (%s, %s)",
                                                (re.findall(r'\d+', line)[0], file[:-3]))
                                database.commit()


insert_id_in_white_list()
update_fm_and_item_id()

import logging

import mysql.connector

HOST: str = "localhost"
LOGIN: str = "root"
PASSWORD: str = "admin"
DATABASE_NAME: str = "bot_mitm"

logger = logging.getLogger(__name__)


class Database:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host=HOST,
            user=LOGIN,
            password=PASSWORD,
            database=DATABASE_NAME,
        )
        logger.info("MySQL connection done")

    def close(self) -> None:
        self.connection.close()

    def select_message_by_protocol_id(self, protocol_id: int) -> str or bool:
        try:
            with self.connection.cursor() as request:
                request.execute("select message_name from message_network where protocol_id = %s", (protocol_id,))
                return request.fetchone()[0]
        except TypeError:
            return False

    def select_protocol_id_by_message_name(self, message_name: str) -> int:
        with self.connection.cursor() as request:
            request.execute("select protocol_id from message_network where message_name = %s", (message_name,))
            return request.fetchone()[0]

    def select_rune_name_by_rune_id(self, rune_id: int) -> str:
        with self.connection.cursor() as request:
            request.execute("select rune_name from rune where rune_id = %s", (rune_id,))
            return request.fetchone()[0]

    def delete_message_network(self) -> None:
        with self.connection.cursor() as request:
            request.execute("delete from message_network")
            self.connection.commit()

    def delete_all_rune(self) -> None:
        with self.connection.cursor() as request:
            request.execute("delete from rune")
            self.connection.commit()

    def insert_rune(self, rune_id: int, rune_name: str, reliquat_weight: float = None) -> None:
        with self.connection.cursor() as request:
            if reliquat_weight is None:
                request.execute("insert into rune(rune_id, rune_name) values (%s, %s)",
                                (rune_id, rune_name))
            else:
                request.execute("insert into rune(rune_id, rune_name, reliquat_weight) values (%s, %s, %s)",
                                (rune_id, rune_name, reliquat_weight))
            self.connection.commit()

    def insert_message_network(self, protocol_id: int, message_name: str) -> None:
        with self.connection.cursor() as request:
            request.execute("insert into message_network(protocol_id, message_name) values (%s, %s)",
                            (protocol_id, message_name))
            self.connection.commit()

    @staticmethod
    def insert_item(target_line: list[dict], name_item: str)-> None:
        connection = mysql.connector.connect(
            host=HOST,
            user=LOGIN,
            password=PASSWORD,
            database=DATABASE_NAME,
        )
        #FIXME FAIRE UNE PROCÉDURE POUR SA
        '''with connection.cursor() as request:
            request.execute("insert into item(name) values (%s)",
                            (name_item,))
            request.execute("insert into target_line(value, item_id, rune_id, line, column) select ",
                            (name_item,))
            connection.commit()'''

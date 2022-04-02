import mysql.connector

from models.item import Item


class DatabaseManagement:
    def __init__(self):
        self.__host = "localhost"
        self.__login = "root"
        self.__password = "root"
        self.__database_name = "bot_sniffer"
        self.__database = mysql.connector.connect(
            host=self.host,
            user=self.login,
            password=self.password,
            database=self.database_name,
        )

    @property
    def host(self):
        return self.__host

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def database_name(self):
        return self.__database_name

    @property
    def database(self):
        return self.__database

    def close(self):
        self.database.close()

    def select_all_items(self) -> list[str]:
        items = []
        with self.database.cursor() as request:
            request.execute("select * from item")
            results = request.fetchall()
            for item in results:
                items.append(item[0])
        return items

    def select_target_lines_by_name_item(self, name) -> list[list[str], list[int], list[int], list[int]]:
        target_lines = []
        type_runes = []
        value_runes = []
        line_runes = []
        column_rune = []

        with self.database.cursor() as request:
            request.execute("select type_rune, value_rune, line_rune, column_rune from target_line "
                            "where name_item = %s", (name,))
            results = request.fetchall()
            for item in results:
                type_runes.append(item[0])
                value_runes.append(item[1])
                line_runes.append(item[2])
                column_rune.append(item[3])

        target_lines.append(type_runes)
        target_lines.append(value_runes)
        target_lines.append(line_runes)
        target_lines.append(column_rune)
        return target_lines

    def insert_or_update_target_lines_item(self, item: Item()):

        if not self.check_if_item_exists(item.name):
            self.insert_item(item.name)

        self.drop_target_lines_item(item.name)
        with self.database.cursor() as request:
            for i in range(len(item.type_runes)):
                request.execute("insert into target_line(type_rune, value_rune, line_rune, "
                                "column_rune, name_item) values ( "
                                "%s, %s, %s, %s, %s)", (
                                    item.type_runes[i], item.value_runes[i], item.line_runes[i], item.column_runes[i],
                                    item.name))
            self.database.commit()

    def drop_target_lines_item(self, name: str):
        with self.database.cursor() as request:
            request.execute("delete from target_line where name_item = (%s)", (name,))
            self.database.commit()

    def insert_item(self, name: str):
        with self.database.cursor() as request:
            request.execute("insert into item(name) values (%s)", (name,))
            self.database.commit()

    def check_if_item_exists(self, name: str) -> bool:
        with self.database.cursor() as request:
            request.execute("select count(*) from item where item.name = (%s)", (name,))
            count_item = request.fetchone()
            return count_item[0]

    def drop_item(self, name: str):
        with self.database.cursor() as request:
            request.execute("delete from item where item.name = (%s)", (name,))
            self.database.commit()

    def check_if_id_in_white_list(self, packet_id: int) -> bool:
        with self.database.cursor() as request:
            request.execute("select count(*) from white_list where white_list_id = %s", (packet_id,))
            count_white_list = request.fetchone()
            return count_white_list[0]

    def select_types_rune_by_runes_id(self, runes_id: list[int]) -> list:
        types_rune = []
        with self.database.cursor() as request:
            for rune_id in runes_id:
                request.execute("select name from rune where dofus_id = %s", (rune_id,))
                result = request.fetchone()
                if result is not None:
                    types_rune.append(result[0])
        return types_rune

    def select_runes_id_by_types_rune(self, types_rune: list[str]) -> list:
        id_runes = []
        with self.database.cursor() as request:
            for type_rune in types_rune:
                request.execute("select dofus_id from rune where name = %s", (type_rune,))
                result = request.fetchone()
                if result is not None:
                    id_runes.append(result[0])
        return id_runes

    def change_item_name(self, old_name, new_name):
        with self.database.cursor() as request:
            request.execute("update item set name = %s where name = %s", (new_name, old_name))
            self.database.commit()

    def select_needed_message_network(self) -> list[int, int]:
        with self.database.cursor() as request:
            request.execute("select id_message from message_network where name_message = (%s or %s)",
                            ("ExchangeCraftResultMagicWithObjectDescMessage", "ExchangeObjectAddedMessage"))
            result = request.fetchall()
        return result

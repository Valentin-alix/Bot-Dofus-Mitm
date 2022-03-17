import mysql.connector


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

    def select_target_lines_by_name_item(self, name) -> list[list[str], list[int], list[int], list[int], list[int]]:
        target_lines = []
        with self.database.cursor() as request:
            request.execute("select type_rune, id_type_rune, value_rune, line_rune, column_rune from target_line "
                            "where name_item = %s", (name,))
            results = request.fetchall()
            for item in results:
                target_lines.append(item)
        return target_lines

    def insert_or_update_target_lines_item(self, name: str, types_runes: list[str],
                                           values_runes: list[int],
                                           lines_runes: list[int],
                                           columns_rune: list[int]):

        if not self.check_if_item_exists(name):
            self.insert_item(name)

        self.drop_target_lines_item(name)
        with self.database.cursor() as request:
            for i in range(len(types_runes)):
                request.execute("insert into target_line(type_rune, value_rune, line_rune, "
                                "column_rune, name_item) values ( "
                                "%s, %s, %s, %s, %s)", (
                                    types_runes[i], values_runes[i], lines_runes[i], columns_rune[i],
                                    name))
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

    def select_types_rune_by_runes_id(self, rune_id: list[int]) -> list:
        types_rune = []
        with self.database.cursor() as request:
            for i in range(len(rune_id)):
                request.execute("select name from rune where dofus_id = %s", (rune_id[i],))
                result = request.fetchone()
                if result is not None:
                    types_rune.append(result[0])
        return types_rune

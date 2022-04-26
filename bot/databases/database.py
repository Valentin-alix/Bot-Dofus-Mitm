import mysql.connector

from bot.models.item import Item


class Database:
    HOST: str = "localhost"
    LOGIN: str = "root"
    PASSWORD: str = ""
    DATABASE_NAME: str = "bot_sniffer"

    def __init__(self):
        self.__connection = mysql.connector.connect(
            host=self.HOST,
            user=self.LOGIN,
            password=self.PASSWORD,
            database=self.DATABASE_NAME,
        )

    @property
    def connection(self):
        return self.__connection

    def close(self) -> None:
        self.connection.close()

    def select_all_name_items(self) -> list[str]:
        items = []
        with self.connection.cursor() as request:
            request.execute("select * from item")
            results = request.fetchall()
            for item in results:
                items.append(item[0])
        return items

    def select_item_by_name(self, name: str) -> Item:
        item = Item()
        item.name = name
        with self.connection.cursor() as request:
            request.execute("select type_rune, value_rune, line_rune, column_rune from target_line "
                            "where name_item = %s", (name,))
            results = request.fetchall()
            for result in results:
                item.runes.append({"type": result[0], "value": result[1], "line": result[2], "column": result[3]})

        return item

    def insert_or_update_item(self, item: Item) -> None:

        if not self.check_if_item_exists(item.name):
            self.insert_item_name(item.name)

        self.delete_target_line_item(item.name)
        with self.connection.cursor() as request:
            for rune in item.runes:
                request.execute("insert into target_line(type_rune, value_rune, line_rune, "
                                "column_rune, name_item) values ( "
                                "%s, %s, %s, %s, %s)", (
                                    rune.get("type"), rune.get("value"), rune.get("line"), rune.get("column"),
                                    item.name))
            self.connection.commit()

    def delete_target_line_item(self, name: str) -> None:
        with self.connection.cursor() as request:
            request.execute("delete from target_line where name_item = (%s)", (name,))
            self.connection.commit()

    def insert_item_name(self, name: str) -> None:
        with self.connection.cursor() as request:
            request.execute("insert into item(name) values (%s)", (name,))
            self.connection.commit()

    def check_if_item_exists(self, name: str) -> bool:
        with self.connection.cursor() as request:
            request.execute("select count(*) from item where item.name = (%s)", (name,))
            count_item = request.fetchone()
            return count_item[0]

    def drop_item_name(self, name: str) -> None:
        with self.connection.cursor() as request:
            request.execute("delete from item where item.name = (%s)", (name,))
            self.connection.commit()

    def change_item_name(self, old_name: str, new_name: str) -> None:
        with self.connection.cursor() as request:
            request.execute("update item set name = %s where name = %s", (new_name, old_name))
            self.connection.commit()

    def select_id_by_message(self, name_message: str) -> int:
        with self.connection.cursor() as request:
            request.execute("select id_message from message_network where name_message = %s",
                            (name_message,))
            result = request.fetchone()
        return result[0]

    def select_message_by_id(self, id_message: int) -> str or bool:
        try:
            with self.connection.cursor() as request:
                request.execute("select name_message from message_network where id_message = %s",
                                (id_message,))
                result = request.fetchone()
            return result[0]
        except TypeError:
            return False

    def select_weight_by_rune_id(self, rune_id: int) -> float:
        with self.connection.cursor() as request:
            request.execute("select reliquat_weight from rune where dofus_id = %s",
                            (rune_id,))
            result = request.fetchone()
        return result[0]

    def select_type_rune_by_id(self, rune_id: int) -> str:
        with self.connection.cursor() as request:
            request.execute("select name from rune where dofus_id = %s", (rune_id,))
            result = request.fetchone()
        return result[0]

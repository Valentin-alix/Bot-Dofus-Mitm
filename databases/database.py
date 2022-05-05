import mysql.connector

from models.item import Item

HOST: str = "localhost"
LOGIN: str = "root"
PASSWORD: str = ""
DATABASE_NAME: str = "bot_sniffer"


class Database:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host=HOST,
            user=LOGIN,
            password=PASSWORD,
            database=DATABASE_NAME,
        )

    def close(self) -> None:
        self.connection.close()

    def select_all_name_items(self) -> list[str]:
        with self.connection.cursor() as request:
            request.execute("select name from item")
            return list(sum(request.fetchall(), ()))

    def select_item_by_name(self, name: str) -> Item:
        item = Item()
        item.name = name
        with self.connection.cursor() as request:
            request.execute("select type_rune, value_rune, line_rune, column_rune from target_line "
                            "where name_item = %s", (name,))
            [item.runes.append({"type": result[0], "value": result[1], "line": result[2], "column": result[3]}) for
             result in request.fetchall()]
        return item

    def insert_or_update_item(self, item: Item) -> None:

        if not self.check_if_item_exists(item.name):
            self.insert_item_name(item.name)

        self.delete_target_line_item(item.name)
        with self.connection.cursor() as request:
            [request.execute(
                "insert into target_line(type_rune, value_rune, line_rune, column_rune, name_item) values ( "
                "%s, %s, %s, %s, %s)", (
                    rune.get("type"), rune.get("value"), rune.get("line"), rune.get("column"),
                    item.name)) for rune in item.runes]
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
            return request.fetchone()[0]

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
            return request.fetchone()[0]

    def select_message_by_id(self, id_message: int) -> str or bool:
        try:
            with self.connection.cursor() as request:
                request.execute("select name_message from message_network where id_message = %s",
                                (id_message,))
                return request.fetchone()[0]
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

    def update_quantity_on_target_line_by_type_rune(self, type_rune: str, name_item: str, quantity: int) -> None:
        with self.connection.cursor() as request:
            request.execute("update target_line set quantity=quantity+%s where type_rune = %s and name_item = %s",
                            (quantity, type_rune, name_item))
            self.connection.commit()

    def update_exo_on_item_by_name(self, name: str) -> None:
        with self.connection.cursor() as request:
            request.execute("update item set attempt=attempt+1 where name = %s", (name,))
            self.connection.commit()

    def update_average_price_by_name(self, name: str, average_price: int) -> None:
        with self.connection.cursor() as request:
            request.execute("update rune set average_price = %s where name = %s", (average_price, name))
            self.connection.commit()

    def update_item_id_by_name(self, name: str, item_id: int) -> None:
        with self.connection.cursor() as request:
            request.execute("update rune set item_id = %s where name = %s", (item_id, name))
            self.connection.commit()

    def select_name_by_item_id(self, item_id: int) -> str or bool:
        try:
            with self.connection.cursor() as request:
                request.execute("select name from rune where item_id = %s",
                                (item_id,))
                return request.fetchall()
        except TypeError:
            return False

    def select_price_item_per_tenta(self, name: str) -> int:
        try:
            with self.connection.cursor() as request:
                request.execute("select rune.name, rune.average_price*target_line.quantity as price_rune from rune "
                                "join "
                                "target_line on target_line.type_rune = rune.name WHERE target_line.name_item = %s;",
                                (name,))
                total_price: int = sum(result[1] for result in request.fetchall())
                request.execute("select item.attempt from item where item.name = %s", (name,))
                return round(total_price / request.fetchone()[0], 1)
        except ZeroDivisionError:
            return 0

import logging
import eel
from mysql.connector import connect, Error

logger = logging.getLogger(__name__)

HOST: str = "localhost"
LOGIN: str = "root"
PASSWORD: str = "admin"
DATABASE_NAME: str = "bot_mitm"

try:
    connection =  connect(host=HOST, user=LOGIN, password=PASSWORD, database=DATABASE_NAME)
    logger.info("MySQL connection done")
except Error as e:
    print(e)
    logger.info("MySQL connection error")


@eel.expose
def insert_item(target_line: list[dict], name_item: str) -> None:
    logger.info(f"Updating Database with : {name_item} | {target_line}")
    {'Type': 'Vitalité', 'Value': '217', 'Line': '0', 'Column': '0'}
    with connection.cursor() as request:
        request.execute("insert into item(name) values (%s)",
                        (name_item,))
        connection.commit()
        for line in target_line:
            request.execute("call insert_target_line(%s,%s,%s,%s,%s)",
                            (line['Value'], name_item, line['Type'], line['Line'], line['Column']))
        connection.commit()


@eel.expose
def get_all_items():
    with connection.cursor() as request:
        request.execute("select name, attempts from item")
        return request.fetchall()


@eel.expose
def delete_item(name_item: str) -> None:
    with connection.cursor() as request:
        request.execute(
            "delete target_line.* from target_line join item on target_line.item_id = item.id where item.name = %s", (name_item,))
        connection.commit()
        request.execute("delete from item where name = %s", (name_item,))
        connection.commit()


def select_message_by_protocol_id(protocol_id: int) -> str or bool:
    try:
        with connection.cursor() as request:
            request.execute(
                "select message_name from message_network where protocol_id = %s", (protocol_id,))
            return request.fetchone()[0]
    except TypeError:
        return False


def select_protocol_id_by_message_name(message_name: str) -> int:
    with connection.cursor() as request:
        request.execute(
            "select protocol_id from message_network where message_name = %s", (message_name,))
        return request.fetchone()[0]


def select_rune_name_by_rune_id(rune_id: int) -> str:
    with connection.cursor() as request:
        request.execute(
            "select rune_name from rune where rune_id = %s", (rune_id,))
        return request.fetchone()[0]


def select_target_line_by_name(item_name: str) -> list[tuple]:
    with connection.cursor(dictionary=True) as request:
        request.execute("select `value`, rune.rune_name, line, `column` from target_line join rune on target_line.rune_id = rune.id join item on item.id = target_line.item_id where item.name = %s;", (item_name,))
        return request.fetchall()


def select_name_by_object_id(object_id: int) -> str or bool:
    try:
        with connection.cursor() as request:
            request.execute(
                "select rune_id from rune where object_id = %s", (object_id,))
            return request.fetchall()
    except TypeError:
        return False


def delete_message_network() -> None:
    with connection.cursor() as request:
        request.execute("delete from message_network")
        connection.commit()


def delete_all_rune() -> None:
    with connection.cursor() as request:
        request.execute("delete from rune")
        connection.commit()


def insert_rune(rune_id: int, rune_name: str, reliquat_weight: float = None) -> None:
    with connection.cursor() as request:
        if reliquat_weight is None:
            request.execute("insert into rune(rune_id, rune_name) values (%s, %s)",
                            (rune_id, rune_name))
        else:
            request.execute("insert into rune(rune_id, rune_name, reliquat_weight) values (%s, %s, %s)",
                            (rune_id, rune_name, reliquat_weight))
        connection.commit()


def update_average_price_by_name(type_rune: str, average_price: int) -> None:
    with connection.cursor() as request:
        request.execute("update rune set average_price = %s where rune_name = %s",
                        (average_price, type_rune))
        connection.commit()


def update_object_id_by_rune_id(object_id: int, rune_id: int) -> None:
    with connection.cursor() as request:
        request.execute("update rune set object_id = %s where rune_id = %s",
                        (object_id, rune_id))
        connection.commit()


def insert_message_network(protocol_id: int, message_name: str) -> None:
    with connection.cursor() as request:
        request.execute("insert into message_network(protocol_id, message_name) values (%s, %s)",
                        (protocol_id, message_name))
        connection.commit()

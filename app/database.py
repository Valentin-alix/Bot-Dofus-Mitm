import logging
import sqlite3
import threading

logger = logging.getLogger(__name__)

connections = {}


def clear_connections():
    global connections
    for key, value in connections.items():
        value.close()
    connections = {}


def get_connection():
    try:
        if connections.get(threading.get_ident(), None) is None:
            connections[threading.get_ident()] = sqlite3.connect("sqlite3.db")
            logger.info("connection done")
        return connections[threading.get_ident()]
    except Exception as e:
        logger.info(f"connection error : {e}")


def execute_sql(raw_sql, args=[], is_execute_many=False):
    connection: sqlite3.Connection = get_connection()
    cursor = connection.cursor()
    if is_execute_many:
        request = cursor.executemany(raw_sql, args)
    else:
        request = cursor.execute(raw_sql, args)

    if "select" in raw_sql.lower():
        results = request.fetchall()
        return results
    else:
        connection.commit()

from enum import Enum
import logging
import socket

logger = logging.getLogger(__name__)

FILTER_DOFUS = "tcp port 5555"

BIT_RIGHT_SHIFT_LEN_PACKET_ID = 2
BIT_MASK = 3


def get_local_ip() -> str:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0)
    try:
        sock.connect(("10.255.255.255", 1))
        ip_local = sock.getsockname()[0]
        logger.info(msg=f"Local ip = {ip_local}")
    except Exception as err:
        logger.error(f"Exception on get local ip : {err}")
        ip_local = "127.0.0.1"
    finally:
        sock.close()
    return ip_local

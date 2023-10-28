import logging

from models.data import Data

logger = logging.getLogger(__name__)


class ExchangeCraftResultMagicWithObjectDescMessage:
    @staticmethod
    def deserialize(data: Data):
        message = {}

        message["craft_result"] = data.readByte()
        message["item_updated_id"] = data.readVarUhInt()

        message["item"] = []

        message["effects_len"] = int(data.readUnsignedShort())
        for _ in range(message["effects_len"]):
            message["id2"] = int(data.readUnsignedShort())
            message["item"].append(
                {
                    "rune_id": data.readVarUhShort(),
                    "value": data.readVarUhInt(),
                }
            )

        message["object_UID"] = data.readVarUhInt()
        message["quantity"] = data.readVarInt()

        message["magic_pool_status"] = data.readByte()

        ExchangeCraftResultMagicWithObjectDescMessage.on_receive(message)

        return message

    def on_receive(message):
        logger.info(message)

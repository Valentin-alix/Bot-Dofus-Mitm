from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from sqlalchemy.orm import sessionmaker

from app.database.models import get_engine, TypeItem
from app.network.utils import send_parsed_msg
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseSearchMessage import \
    ExchangeBidHouseSearchMessage

if TYPE_CHECKING:
    from app.types_.models.common import CommonInfo
    from app.types_.dicts.selling import SelectedObject

logger = logging.getLogger(__name__)


class Hdv:
    def __init__(self, common_info: CommonInfo):
        self.common_info = common_info
        self.selected_object: SelectedObject | None = None
        self.engine = get_engine()

        # TODO Close object at stop playing

    def place_object(self, object_gid: int):
        logger.info(f"Sending place object {object_gid}")
        send_parsed_msg(
            self.common_info.message_to_send_queue,
            ExchangeBidHouseSearchMessage(
                objectGID=object_gid,
                follow=True,
            ),
        )

    def close_selected_object(self):
        assert self.selected_object is not None
        send_parsed_msg(
            self.common_info.message_to_send_queue,
            ExchangeBidHouseSearchMessage(
                follow=False,
                objectGID=self.selected_object["object_gid"],
            ),
        )
        logger.info(
            f"sending ExchangeBidHouseSearchMessage with objectGID : {self.selected_object['object_gid']} to "
            f"close"
        )

    def get_accepted_types(self, types_id: list[int]) -> list[int]:
        """filter type item to be in database"""
        with sessionmaker(bind=self.engine)() as session:
            accepted_types = [
                _type.id
                for _type in (
                    session.query(TypeItem.id)
                    .filter(TypeItem.id.in_(types_id))
                    .all()
                )
            ]
        return accepted_types

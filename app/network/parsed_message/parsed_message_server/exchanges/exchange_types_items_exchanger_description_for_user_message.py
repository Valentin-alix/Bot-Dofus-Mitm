import logging
from datetime import datetime

import types_
from database.models import Object, Price, get_engine
from network.parsed_message.dicts import BidExchangerObjectInfo
from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)


class ExchangeTypesItemsExchangerDescriptionForUserMessage(ParsedMessageServer):
    """Receivied hdv object prices after clicking in objects"""

    itemTypeDescriptions: list[BidExchangerObjectInfo]
    objectGID: int
    objectType: int

    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        logger.info("Got prices of objects")
        if len(self.itemTypeDescriptions) == 1:
            engine = get_engine()
            session = sessionmaker(bind=engine)()
            # Saving prices in database
            _object = session.query(Object).filter_by(object_gid=self.objectGID).first()
            if _object is not None:
                prices_values = ",".join(
                    str(price) for price in self.itemTypeDescriptions[0].get("prices")
                )
                price = Price(
                    creation_date=datetime.now(),
                    object_id=_object.id,
                    list_prices=prices_values,
                )
                session.add(price)
                session.commit()

                session.close()

        with threads_infos.get("buying_hdv_with_lock").get("lock"):
            if (
                buying_hdv := threads_infos.get("buying_hdv_with_lock").get(
                    "buying_hdv"
                )
            ) is not None:
                if threads_infos.get("event_play_hdv_scrapping").is_set():
                    buying_hdv.process()

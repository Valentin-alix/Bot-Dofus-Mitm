from dataclasses import dataclass
from datetime import datetime
from blinker import signal
from copy import deepcopy
from sqlalchemy.orm import sessionmaker
from database.models import Object, Price, get_engine
from types_ import (
    ExchangeBidHouseSearchMessage,
    ExchangeTypesExchangerDescriptionForUserMessage,
    ExchangeTypesItemsExchangerDescriptionForUserMessage,
    SellerBuyerDescriptor,
)
from types_.interface import ExchangeBidHouseTypeMessage


class Hdv:
    categories: list[int]
    types_object: list[dict] = []

    def __init__(self, seller_buyer_descriptor: SellerBuyerDescriptor):
        self.seller_buyer_descriptor = seller_buyer_descriptor
        self.categories = self.seller_buyer_descriptor.get("types")
        self.msg_to_send_signal = signal("send_message")

        self.check_all_category()

    def check_all_category(self):
        for category in self.categories:
            exchange_bid_house_type_message_exchange_bid_house_type_message = (
                ExchangeBidHouseTypeMessage(
                    __type__="ExchangeBidHouseTypeMessage",
                    from_client=True,
                    follow=True,
                    type=category,
                )
            )
            self.msg_to_send_signal.send(
                exchange_bid_house_type_message_exchange_bid_house_type_message
            )

    def on_received_opened_category(
        self, parsed_message: ExchangeTypesExchangerDescriptionForUserMessage
    ):
        for type_description in parsed_message.typeDescription:
            self.types_object.append(
                {"object_gid": type_description, "is_opened": True}
            )

        if len(self.types_object) > 0:
            self.send_get_price_object_gid(self.types_object[-1])

    def send_get_price_object_gid(self, type_object: dict):
        exchange_bid_house_search_message = ExchangeBidHouseSearchMessage(
            __type__="ExchangeBidHouseSearchMessage",
            from_client=True,
            objectGID=type_object.get("object_gid"),
            follow=type_object.get("is_opened"),
        )
        self.msg_to_send_signal.send(exchange_bid_house_search_message)

    def on_receive_get_prices_gid(
        self, parsed_message: ExchangeTypesItemsExchangerDescriptionForUserMessage
    ):
        engine = get_engine()
        session = sessionmaker(bind=engine)()

        if len(parsed_message.itemTypeDescriptions) == 1:
            _object = (
                session.query(Object)
                .filter_by(object_gid=parsed_message.objectGID)
                .first()
            )
            if _object is not None:
                prices_values = ",".join(
                    str(price)
                    for price in parsed_message.itemTypeDescriptions[0].get("prices")
                )
                price = Price(
                    creation_date=datetime.now(),
                    object_id=_object.id,
                    list_prices=prices_values,
                )
                session.add(price)
                session.commit()

                session.close()

        if len(self.types_object) > 0:
            type_object = self.types_object[-1]
            if type_object.get("is_opened") is True:
                type_object["is_opened"] = False
                self.send_get_price_object_gid(type_object)
            else:
                self.types_object.pop()
                type_object = self.types_object[-1]
                self.send_get_price_object_gid(type_object)

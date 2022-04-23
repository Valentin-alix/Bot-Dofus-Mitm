from databases.database_management import DatabaseManagement
from factory import action
from gui import interface

ExchangeObjectAddedMessage: int = DatabaseManagement().select_id_by_message("ExchangeObjectAddedMessage")
ExchangeCraftResultMagicWithObjectDescMessage: int = DatabaseManagement().select_id_by_message(
    "ExchangeCraftResultMagicWithObjectDescMessage")


def interpretation(message):
    if str(message).startswith("ExchangeObjectAddedMessage") and not action.bot_is_playing:
        if len(message.object.effects) > 1:
            types_rune = []
            values_rune = []
            for effect in message.object.effects:
                types_rune.append(effect.actionId)
                values_rune.append(effect.value)

            interface.inserted_item.id_runes = types_rune
            interface.inserted_item.value_runes = values_rune
            interface.interface.clear_frame(interface.interface.root)
            interface.interface.ajout_item_window()

    elif str(message).startswith("ExchangeCraftResultMagicWithObjectDescMessage") and action.bot_is_playing:
        types_rune = []
        values_rune = []
        for effect in message.objectInfo.effects:
            types_rune.append(effect.actionId)
            values_rune.append(effect.value)

        action.item.actual_id_values = types_rune

        action.item.actual_values = values_rune

        action.click_based_on_values()

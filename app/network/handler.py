def handle_message_content(content: dict, message_type):
    if message_type == "ExchangeCraftResultMagicWithObjectDescMessage":
        print(content)
    elif message_type == "ExchangeObjectAddedMessage":
        print(content)

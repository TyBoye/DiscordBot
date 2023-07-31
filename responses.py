import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Hey You"

    if p_message == "spam":
        return "spam"
    
    if p_message == "rolldice":
        return str(random.randint(1, 6))

    if =_message == ""


    if p_message == "help":
        return "`rolldice\nspam\nhello`"

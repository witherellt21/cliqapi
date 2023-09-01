from random import choices
import string


def generate_user_identifier():
    return "user_" + "".join(choices(string.ascii_letters + string.digits, k=27))

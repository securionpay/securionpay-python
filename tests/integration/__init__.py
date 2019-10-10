import random
import string


def random_string():
    return "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase)
        for _ in range(10)
    )


def random_email():
    return random_string() + "@" + random_string() + ".com"

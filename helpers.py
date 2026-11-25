import random
import string

from data import COHORT


def generate_email():
    return f'irinasvyatkina{COHORT}{random.randint(100, 999)}@yandex.ru'


def generate_password(length=8):
    symbols = string.ascii_letters + string.digits
    return ''.join(random.choice(symbols) for _ in range(length))

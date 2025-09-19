import time
from faker import Faker

fake = Faker("ru_RU")

def get_random_email() -> str:
    return f"test.{time.time()}@example.com"


def get_random_first_name() -> str:
    return fake.first_name()

def get_random_last_name() -> str:
    return fake.last_name()

def get_random_middle_name() -> str:
    return fake.middle_name()

def get_random_password() -> str:
    return fake.password(length=8)


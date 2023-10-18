from random import random
from redisx.client import Client

# change the following configuration for your Tair.
REDIS_HOST = "localhost"
REDIS_PORT = 6666
REDIS_DB = 0
REDIS_USERNAME = ""
REDIS_PASSWORD = ""


def get_client() -> Client:
    return Client(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        username=REDIS_USERNAME,
        password=REDIS_PASSWORD,
    )


def get_random_vectors(dim: int, n: int):
    return [[random() for _ in range(dim)] for _ in range(n)]

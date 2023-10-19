import os
from datetime import datetime
from typing import Union
from random import random

import pytest
from redisx.client import Client, ClusterClient

# change the following configuration for your redis
REDIS_HOST = "localhost"
REDIS_PORT = 6363
REDIS_DB = 0
REDIS_USERNAME = ""
REDIS_PASSWORD = ""

REDIS_CLUSTER_HOST = "localhost"
REDIS_CLUSTER_PORT = 30000
REDIS_CLUSTER_USERNAME = None
REDIS_CLUSTER_PASSWORD = None


def get_client() -> Client:
    return Client(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        username=REDIS_USERNAME,
        password=REDIS_PASSWORD,
    )


def get_cluster_client() -> ClusterClient:
    return ClusterClient(
        host=REDIS_CLUSTER_HOST,
        port=REDIS_CLUSTER_PORT,
        username=REDIS_CLUSTER_USERNAME,
        password=REDIS_CLUSTER_PASSWORD,
    )


# set TEST_REDIS_CLUSTER environment variable to enable cluster mode.
@pytest.fixture()
def uc() -> Union[Client, ClusterClient]:
    if os.environ.get("TEST_CLUSTER_CLIENT") is None:
        cli = get_client()
    else:
        cli = get_cluster_client()
    yield cli
    cli.close()


@pytest.fixture()
def cc() -> ClusterClient:
    cli = get_cluster_client()
    yield cli
    cli.close()


def get_random_vectors(dim: int, n: int):
    return [[random() for _ in range(dim)] for _ in range(n)]


def get_server_time(client) -> datetime:
    seconds, milliseconds = client.time()
    timestamp = float(f"{seconds}.{milliseconds}")
    return datetime.fromtimestamp(timestamp)


def compare_str(left, right):
    if isinstance(left, bytes):
        left = left.decode()
    if isinstance(right, bytes):
        right = right.decode()

    return left == right

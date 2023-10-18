#!/usr/bin/env python3
from random import random
from conf_cases import get_client
from redis import ResponseError

dim = 4
queries = [[random() for _ in range(dim)] for _ in range(2)]


# create an index
# @param index_name the name of index
# @param dims the dimension of vector
# @return success: true, fail: none.
def create_index(index_name: str):
    try:
        cli = get_client()
        # index_params the params of index
        return cli.create_index(index_name, dim)
    except ResponseError as e:
        print(e)
        return None


# get an index
# @param index_name the name of index
# @return success: dict info, fail: none.
def get_index(index_name: str):
    try:
        # index_params the params of index
        return get_client().get_index(index_name)
    except ResponseError as e:
        print(e)
        return None


# delete an index
# @param index_name the name of index
# @return success: 1, fail: none.
def delete_index(index_name: str):
    try:
        return get_client().del_index(index_name)
    except ResponseError as e:
        print(e)
        return False


if __name__ == "__main__":
    create_index("test")
    get_index("test")
    delete_index("test")

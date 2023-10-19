#!/usr/bin/env python3
from conf_cases import get_client, get_random_vectors
from redis import ResponseError
from redisx.define import UsearchQuantizationType

cli = get_client()


# create an index
# @param index_name the name of index
# @param dim the dimension of vector
# @return success: true, fail: None.
def create_index(index_name: str, dim: int):
    try:
        return cli.create_index(
            index_name, dim,
            quantization=UsearchQuantizationType.F64)
    except ResponseError as e:
        print(e)
        return None


# get an index
# @param index_name the name of index
# @return success: dict info, fail: None.
def get_index(index_name: str):
    try:
        return cli.get_index(index_name)
    except ResponseError as e:
        print(e)
        return None


# delete an index
# @param index_name the name of index
# @return success: 1, fail: False.
def delete_index(index_name: str):
    try:
        return cli.del_index(index_name)
    except ResponseError as e:
        print(e)
        return False


# add vector
# @param index_name the name of index
# @param name the name of vector node name
# @param vector vector data
# @return success: vector info, fail: None.
def add_vector(index_name: str, name: str, vector: []):
    try:
        return cli.add_vector(index_name, name, vector)
    except ResponseError as e:
        print(e)
        return None


# get vector
# @param index_name the name of index
# @param name the name of vector node name
# @return success: vector info, fail: None.
def get_vector(index_name: str, name: str):
    try:
        return cli.get_vector(index_name, name)
    except ResponseError as e:
        print(e)
        return None


# del vector
# @param index_name the name of index
# @param name the name of vector node name
# @return success: vector info, fail: False.
def del_vector(index_name: str, name: str):
    try:
        return cli.del_vector(index_name, name)
    except ResponseError as e:
        print(e)
        return False


# add vector id
# @param index_name the name of index
# @param name the name of vector node name
# @param vector vector data
# @return success: vector info, fail: None.
def add_vector_id(index_name: str, id: int, vector: []):
    try:
        return cli.add_vector_id(index_name, id, vector)
    except ResponseError as e:
        print(e)
        return None


# get vector by id
# @param index_name the name of index
# @param name the name of vector node name
# @return success: vector info, fail: None.
def get_vector_id(index_name: str, id: int):
    try:
        return cli.get_vector_id(index_name, id)
    except ResponseError as e:
        print(e)
        return None


# del vector by id
# @param index_name the name of index
# @param id the name of vector id
# @return success: vector info, fail: False.
def del_vector_id(index_name: str, id: int):
    try:
        return cli.del_vector_id(index_name, id)
    except ResponseError as e:
        print(e)
        return False


# kANN search
# @param index_name the name of index
# @param k return k ANN vectors
# @param query_vector  query vector data
# @return success: kAnn vectors, fail: None
def kann_search(index_name: str, k: int, query_vector: []):
    try:
        return cli.kann_search(index_name, k, query_vector)
    except ResponseError as e:
        print(e)
        return False


if __name__ == "__main__":
    dim = 4

    print("delete_index res {}".format(delete_index("test_idx0")))
    print("create_index res {}".format(create_index("test_idx0", dim)))
    print("get_index res {}".format(get_index("test_idx0")))
    for i, vector in enumerate(get_random_vectors(dim, 2)):
        name = "n%i" % i
        print("add_vector {} {} res {}".format(
            name, vector, add_vector("test_idx0", name, vector)))
        print("get_vector res {}".format(get_vector("test_idx0", name)))
        print("del_vector res {}".format(del_vector("test_idx0", name)))
    for i, vector in enumerate(get_random_vectors(dim, 2)):
        print("add_vector_id {} {} res {}".format(
            i, vector, add_vector_id("test_idx0", i, vector)))
        print("get_vector_id res {}".format(get_vector_id("test_idx0", i)))
        print("del_vector_id res {}".format(del_vector_id("test_idx0", i)))

    print("\n======= kann search =====\n")
    for i, vector in enumerate(get_random_vectors(dim, 100)):
        name = "n%i" % i
        print("add_vector {} {} res {}".format(
            name, vector, add_vector("test_idx0", name, vector)))
        # print("get_vector res {}".format(get_vector("test_idx0", name)))
    for i, vector in enumerate(get_random_vectors(dim, 100)):
        print("add_vector_id {} {} res {}".format(
            i, vector, add_vector_id("test_idx0", i, vector)))
        # print("get_vector_id res {}".format(get_vector_id("test_idx0", i)))

    k = 10
    for i, query_vector in enumerate(get_random_vectors(dim, 3)):
        print("{}. kann_search k {} query_vector {} res {}".format(
            i, k, query_vector,
            kann_search("test_idx0", k, query_vector)))

    print("delete_index res {}".format(delete_index("test_idx0")))
    cli.close()

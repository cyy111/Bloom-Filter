import hashlib


def genHashFamily(k):
    """
    :param k: the number of hash funcs in hash family
    :return k hash functions: a list
    """

    result = [hashlib.md5() for i in range(k)]

    for j in range(k):
        result[j].update(str(j).encode())

    return result




import hashlib


def genHashFamily(k):
    """generate k hash functions as hash family"""

    result = [hashlib.md5() for i in range(k)]

    for j in range(k):
        result[j].update(str(j).encode())

    return result


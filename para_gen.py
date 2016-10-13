import math


def gen_m(n, falsePositive):
    """m is the length of bit array"""

    return int(1.44 * n * (math.log(1 / falsePositive, 2)))


def gen_k(m, n):
    """k is the number of hash function in hash family"""

    return int(math.log(2, math.e) * (m / n))

import para_gen
import Hash_Family


def genBitArray(hashFamily, wordSet, m):
    """

    :param hashFamily: a func list
    :param wordSet: s set val
    :param m: length of bit array
    :return bit array: a binary array
    """

    result = [0 for i in range(m)]

    for word in wordSet:
        for hashFunc in hashFamily:
            temp = hashFunc.copy()
            temp.update(word.encode())
            result[int(temp.hexdigest(), 16) % m] = 1

    return result


def insertWord(wordSet, falsePositive):
    """
    * insert words in the bit array
    :param wordSet: a set
    :param falsePositive:
    :return: a tuple that contains 3 elements: bit array, hash family and parameter (n, m, k)
    """

    n = len(wordSet)
    m = para_gen.gen_m(n, falsePositive)
    k = para_gen.gen_k(m, n)

    parameter = (n, m, k)

    hashFamily = Hash_Family.genHashFamily(k)

    # return 3 info: bit array; hash functions; parameter
    return genBitArray(hashFamily, wordSet, m), hashFamily, parameter


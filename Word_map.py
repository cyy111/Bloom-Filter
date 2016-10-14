import para_gen
import Hash_Family


def genBitArray(hashFamily, wordSet, m):
    """map the hash value of each word in word set to bit array according to hash family"""

    result = [0 for i in range(m)]

    for word in wordSet:
        for hashFunc in hashFamily:
            temp = hashFunc.copy()
            temp.update(word.encode())
            result[int(temp.hexdigest(), 16) % m] = 1

    return result


def insertWord(wordSet, falsePositive):
    """insert words in the bit array"""

    n = len(wordSet)
    m = para_gen.gen_m(n, falsePositive)
    k = para_gen.gen_k(m, n)

    parameter = (n, m, k)

    hashFamily = Hash_Family.genHashFamily(k)

    # return 3 info: bit array; hash functions; parameter
    return genBitArray(hashFamily, wordSet, m), hashFamily, parameter


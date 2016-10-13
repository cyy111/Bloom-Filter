import para_gen
import Hash_Family


def wordMap(hashFamily, wordSet, m):
    """map the hash value of each word in word set to bit array according to hash family"""

    result = [0 for i in range(m)]

    for word in wordSet:
        for hashFunc in hashFamily:
            temp = hashFunc.copy()
            temp.update(word.encode())
            result[int(temp.hexdigest(), 16) % m] = 1

    return result


def genBitArray(wordSet, falsePositive):
    """generate the bit array"""

    n = len(wordSet)
    m = para_gen.gen_m(n, falsePositive)
    k = para_gen.gen_k(m, n)

    hashFamily = Hash_Family.genHashFamily(k)

    return wordMap(hashFamily, wordSet, m)


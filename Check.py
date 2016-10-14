
def checkWord(word, hashFamily, bitArray):
    """check if the word can be map in bit array correctly with hash family"""

    m = len(bitArray)

    for hashFunc in hashFamily:

        temp = hashFunc.copy()
        temp.update(word.encode())
        if bitArray[int(temp.hexdigest(), 16) % m] != 1:
            return False
    return True

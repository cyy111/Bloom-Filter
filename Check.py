
def checkWord(word, hashFamily, bitArray):

    m = len(bitArray)

    for hashFunc in hashFamily:

        temp = hashFunc.copy()
        temp.update(word.encode())
        if bitArray[int(temp.hexdigest(), 16) % m] != 1:
            return False
    return True
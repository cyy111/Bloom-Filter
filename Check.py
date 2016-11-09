
def checkWord(word, hashFamily, bitArray):
    """
    :param word: a string
    :param hashFamily: a list
    :param bitArray: a binary list
    :return: the word in bitArray or not
    """

    m = len(bitArray)

    for hashFunc in hashFamily:

        temp = hashFunc.copy()
        temp.update(word.encode())
        if bitArray[int(temp.hexdigest(), 16) % m] != 1:
            return False
    return True

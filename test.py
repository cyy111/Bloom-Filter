import Word_map
import Check
import split_word


def testFunc(wordSet, falsePositive):
    """

    :param wordSet: a set val
    :param falsePositive:
    :return: the check word belongs to data set or not
    """
    loc = input("please enter the location of begin and end: ")

    # begin and end means the word we should insert to data set
    begin = int(loc.split(",")[0])
    end = int(loc.split(",")[1])

    print(list(wordSet)[begin: end])

    checkWord = input("please enter the word you want to check: ")

    clientData = Word_map.insertWord(wordSet, falsePositive)
    print(Check.checkWord(checkWord, clientData[1], clientData[0]))


if __name__ == "__main__":

    words = split_word.splitWords("A Hole in the Fence")
    falsePositive = 1.69e-5
    
    testFunc(words, falsePositive)

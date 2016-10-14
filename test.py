import Word_map
import Check


def cleanWord(word):
    """clean the word"""

    n = len(word)
    i = n - 1
    while i >= 0 and not word[i].isalpha():
        word = word[:i]
        i -= 1
    return word


def splitWord(file_name):
    """split the word of a file"""

    with open(file_name) as f:
        result = []

        for line in f:
            words = line.strip().split()
            for word in words:
                word = cleanWord(word)
                result.append(word)

        return result


def testFunc(wordSet, falsePositive):
    loc = input("please enter the location of begin and end: ")

    begin = int(loc.split(",")[0])
    end = int(loc.split(",")[1])

    print(wordSet[begin: end])

    checkWord = input("please enter the word you want to check: ")

    clientData = Word_map.insertWord(wordSet, falsePositive)
    print(Check.checkWord(checkWord, clientData[1], clientData[0]))


if __name__ == "__main__":

    words = splitWord("A Hole in the Fence")
    falsePositive = 1.69e-5
    
    testFunc(words, falsePositive)

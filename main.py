import Word_map
import Check

falsePositive = 1.69e-5
words = ["dnwe", "hjferf", "dwederf", "dwefuyi"]

if __name__ == "__main__":

    word = "hjferf"

    clientData = Word_map.insertWord(words, falsePositive)
    print(Check.checkWord(word, clientData[1], clientData[0]))







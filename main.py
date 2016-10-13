import Word_map
import Check
import Hash_Family
import para_gen

falsePositive = 1.69e-5
words = ["dnwe", "hjferf", "dwederf", "dwefuyi"]

n = len(words)
m = para_gen.gen_m(n, falsePositive)
k = para_gen.gen_k(m, n)

bitArray = Word_map.genBitArray(words, falsePositive)
hashFamily = Hash_Family.genHashFamily(k)

if __name__ == "__main__":

    word = "hjferf"
    print(Check.checkWord(word, hashFamily, bitArray))







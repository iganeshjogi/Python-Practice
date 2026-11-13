
def find_longest_word(sentence):

    words = sentence.split()

    longest_word = None

    for i in words:

        if longest_word is None or len(i) > len(longest_word):
            longest_word = i

    return longest_word


sentence = "Python programming is very interesting"

print(find_longest_word(sentence))
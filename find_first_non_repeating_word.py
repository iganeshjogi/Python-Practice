def find_first_non_repeating_word(sentence):

    words = sentence.split()

    frequency = {}

    # Step 1: Count frequency of each word
    for word in words:

        if word in frequency:
            frequency[word] += 1

        else:
            frequency[word] = 1

    # Step 2: Find the first word appearing only once
    for word in words:

        if frequency[word] == 1:
            return word

    return None


sentence = "python java python sql java data"

print(find_first_non_repeating_word(sentence))
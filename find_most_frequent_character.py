def find_most_frequent_character(text):

    if len(text) == 0:
        return None

    frequency = {}

    for i in text:

        if i in frequency:
            frequency[i] += 1

        else:
            frequency[i] = 1

    max_frequency = 0
    most_frequent = None

    for i in text:

        if frequency[i] > max_frequency:
            max_frequency = frequency[i]
            most_frequent = i

    return most_frequent


text = "programming"

print(find_most_frequent_character(text))
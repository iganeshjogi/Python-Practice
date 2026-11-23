def find_longest_unique_substring(text):

    current_substring = []
    longest_length = 0

    for char in text:

        while char in current_substring:
            current_substring.pop(0)

        current_substring.append(char)

        if len(current_substring) > longest_length:
            longest_length = len(current_substring)

    return longest_length


text = "abcabcbb"

print(find_longest_unique_substring(text))
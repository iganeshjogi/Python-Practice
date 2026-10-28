
def find_first_non_repeating_character(text):
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char in text:
        if frequency[char] == 1:
            return char

    return None


print(find_first_non_repeating_character("aabbcde"))
print(find_first_non_repeating_character("aabb"))

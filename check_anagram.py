def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    frequency = {}

    for char in str1:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char in str2:
        if char not in frequency:
            return False

        frequency[char] -= 1

        if frequency[char] < 0:
            return False

    return True


print(check_anagram("listen", "silent"))
print(check_anagram("hello", "world"))
print(check_anagram("aab", "abb"))
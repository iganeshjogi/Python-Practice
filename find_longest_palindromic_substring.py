def find_longest_palindromic_substring(text):

    longest_palindrome = ""

    # Generate all possible substrings
    for i in range(len(text)):

        for j in range(i + 1, len(text) + 1):

            substring = text[i:j]

            # Check whether substring is a palindrome
            rev = ""

            for k in range(len(substring) - 1, -1, -1):
                rev += substring[k]

            if substring == rev:

                if len(substring) > len(longest_palindrome):
                    longest_palindrome = substring

    return longest_palindrome


print(find_longest_palindromic_substring("cbbd"))
# bb

print(find_longest_palindromic_substring("racecar"))
# racecar

print(find_longest_palindromic_substring("abcdef"))
# a
def is_palindrome(word):
    temp = ""

    for i in range(len(word) - 1, -1, -1):
        temp += word[i]

    if word == temp:
        return "Palindrome"
    else:
        return "Not Palindrome"


print(is_palindrome("madam"))
print(is_palindrome("python"))
print(is_palindrome("121"))
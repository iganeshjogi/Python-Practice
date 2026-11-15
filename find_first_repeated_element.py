def find_first_repeated_element(numbers):

    if len(numbers) < 2:
        return None

    seen = []

    for i in numbers:

        if i in seen:
            return i

        else:
            seen.append(i)

    return None


numbers = [4, 5, 2, 4, 3, 5]

print(find_first_repeated_element(numbers))

def find_first_non_repeating_element(numbers):

    frequency = {}

    # Count frequency
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find first non-repeating element
    for num in numbers:
        if frequency[num] == 1:
            return num

    return None


numbers = [4, 5, 1, 2, 0, 4, 5, 1]

print(find_first_non_repeating_element(numbers))
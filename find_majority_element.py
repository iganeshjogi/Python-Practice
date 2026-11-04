def find_majority_element(numbers):

    frequency = {}

    for i in numbers:

        if i in frequency:
            frequency[i] += 1

        else:
            frequency[i] = 1

    threshold = len(numbers) // 2

    for key in frequency:

        if frequency[key] > threshold:
            return key

    return None


print(find_majority_element([3, 3, 4, 2, 3, 3, 3]))
# 3

print(find_majority_element([1, 2, 3, 2, 2, 2, 5]))
# 2

print(find_majority_element([5, 5, 2, 2, 2, 5, 5, 3]))
# None
def find_maximum_difference(numbers):

    if len(numbers) < 2:
        return None

    max_difference = None

    for i in range(len(numbers) - 1):

        for j in range(i + 1, len(numbers)):

            difference = numbers[j] - numbers[i]

            if max_difference is None or difference > max_difference:
                max_difference = difference

    return max_difference


numbers = [2, 3, 10, 6, 4, 8, 1]

result = find_maximum_difference(numbers)

print("Maximum Difference:", result)
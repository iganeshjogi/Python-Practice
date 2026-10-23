
def count_frequency(numbers):
    frequency = {}

    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    return frequency


numbers = [1, 2, 2, 3, 1, 4, 2]
result = count_frequency(numbers)

print(result)
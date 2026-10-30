
numbers = [2, 7, 11, 15]
target = 17

def two_sum(numbers, target):

    for i in range(len(numbers)):

        for j in range(i + 1, len(numbers)):

            if numbers[i] + numbers[j] == target:
                return [i, j]

    return None


print(two_sum(numbers, target))

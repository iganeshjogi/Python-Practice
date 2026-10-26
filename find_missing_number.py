
def find_missing_number(numbers):
    n = len(numbers) + 1

    for i in range(1, n + 1):
        if i not in numbers:
            return i


print(find_missing_number([2, 3, 4, 5]))  # Expected: 1
print(find_missing_number([1, 2, 3, 4]))  # Expected: 5
print(find_missing_number([1, 2, 4, 5, 6]))  # Expected: 3
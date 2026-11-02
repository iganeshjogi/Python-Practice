
def rotate_list(numbers, k):

    if not numbers:
        return []

    k = k % len(numbers)

    temp = []

    for i in range(len(numbers) - k, len(numbers)):
        temp.append(numbers[i])

    for i in range(0, len(numbers) - k):
        temp.append(numbers[i])

    return temp


numbers = [1, 2, 3, 4, 5]
k = 3

print(rotate_list(numbers, k))

def move_zeros_to_end(numbers):
    non_zeros = []
    zeros = []

    for i in numbers:
        if i != 0:
            non_zeros.append(i)

    for j in numbers:
        if j == 0:
            zeros.append(j)

    zeros = non_zeros + zeros

    return zeros


print(move_zeros_to_end([1, 2, 3]))             # Expected: [1, 2, 3]
print(move_zeros_to_end([0, 1, 0, 2, 3]))       # Expected: [1, 2, 3, 0, 0]
print(move_zeros_to_end([0, 1, 0]))             # Expected: [1, 0, 0]
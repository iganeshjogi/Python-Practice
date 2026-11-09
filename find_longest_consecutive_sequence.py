def find_longest_consecutive_sequence(numbers):

    if len(numbers) == 0:
        return 0

    longest = 0

    for i in numbers:

        count = 1
        next_number = i + 1

        while next_number in numbers:
            count += 1
            next_number += 1

        if count > longest:
            longest = count

    return longest


numbers = [5, 2, 3, 10, 4, 1]

print(find_longest_consecutive_sequence(numbers))
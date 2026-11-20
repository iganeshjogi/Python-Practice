def move_negative_numbers_to_beginning(numbers):

    negative = []
    positive = []

    for i in numbers:

        if i < 0:
            negative.append(i)

        else:
            positive.append(i)

    final = negative + positive

    return final

    pass


numbers = [1, -2, 3, -4, 5, -6]

print(move_negative_numbers_to_beginning(numbers))
def find_second_most_frequent_element(numbers):

    frequency = {}

    for i in numbers:

        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    max_freq = None
    second_max_freq = None

    for i in frequency:

        if max_freq is None or frequency[i] > max_freq:
            second_max_freq = max_freq
            max_freq = frequency[i]

        elif frequency[i] < max_freq:
            if second_max_freq is None or frequency[i] > second_max_freq:
                second_max_freq = frequency[i]

    if second_max_freq is None:
        return None

    for i in numbers:
        if frequency[i] == second_max_freq:
            return i

    return None



numbers = [1, 1, 1, 7, 7, 3, 4, 5, 6]

print(find_second_most_frequent_element(numbers))
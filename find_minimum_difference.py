
def find_minimum_difference(numbers):

    if len(numbers) < 2:
        return None

    minimum_difference = None

    for i in range(len(numbers)):

        for j in range(i+1, len(numbers)):

            difference = abs(numbers[i] - numbers[j])

            if minimum_difference is None or difference < minimum_difference:
                minimum_difference = difference

    return minimum_difference


numbers = [10, 20, 60, 45]
print(find_minimum_difference(numbers))
 





    
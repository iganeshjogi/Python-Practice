def find_second_largest(numbers):
    largest = second_largest = None

    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num

        elif num != largest and (
            second_largest is None or num > second_largest
        ):
            second_largest = num

    if second_largest is None:
        print("No second-largest distinct number")
    else:
        print("Second-largest number:", second_largest)


numbers = [12, 35, 1, 10, 34, 1]
find_second_largest(numbers)

def remove_duplicates(numbers):
    temp = []

    for i in numbers:
        if i not in temp:
            temp.append(i)

    return temp


numbers = [1, 2, 5, 4, 5, 4, 5, 8, 9, 7]
print(remove_duplicates(numbers))

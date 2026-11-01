def find_common_elements(list1, list2):

    list3 = []

    for i in list1:
        if i in list2 and i not in list3:
            list3.append(i)

    return list3


list1 = [1, 2, 2, 3]
list2 = [2, 3, 4]

print(find_common_elements(list1, list2))
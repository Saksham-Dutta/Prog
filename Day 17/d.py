def find_common_elements_lc(list1, list2):
    set2=set(list2)
    return [item for item in list1 if item in set2]


list_a = [1, 2, 2, 3, 4]
list_b = [2, 4, 6]

result = find_common_elements_lc(list_a, list_b)
print("Common elements:", result)
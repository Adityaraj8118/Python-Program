def find_common_elements(lst1, lst2):
    common_elements = list(set(lst1) & set(lst2))
    print(f"Common elements: {common_elements}")
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
find_common_elements(list1, list2)

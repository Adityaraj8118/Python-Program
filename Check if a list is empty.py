def check_if_empty(lst):
    if not lst:
        print("The list is empty.")
    else:
        print(f"The list is not empty. It contains {len(lst)} elements.")
        
my_list = []
check_if_empty(my_list)
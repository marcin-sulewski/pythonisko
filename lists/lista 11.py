list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

has_common_member = any(item in list2 for item in list1)
print("Do the lists have at least one common member?", has_common_member)

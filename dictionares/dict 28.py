dict = {'a': ['apple', 'banana', 'cherry'], 'b': ['grape', 'orange', 'kiwi']}


sorted_dict = {key: sorted(value) for key, value in dict.items()}

print(sorted_dict)

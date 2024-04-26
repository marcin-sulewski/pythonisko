dict = {'b': 2, 'c': 3, 'a': 1}

sorted_dict = {key: dict[key] for key in sorted(dict)}

print(sorted_dict)

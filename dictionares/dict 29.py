dict = {'key 1': 1, 'key 2': 2, 'key 3': 3}

new_dict = {key.replace(' ', ''): value for key, value in dict.items()}

print(new_dict)

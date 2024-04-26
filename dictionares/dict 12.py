dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'

if key_to_remove in dict:
    del dict[key_to_remove]
    print("po usunieciu", dict)
else:
    print("nie ma klucza")

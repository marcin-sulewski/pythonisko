list = ['a', 'b', 'c']

dict = {}

for key in reversed(list):
    dict = {key: dict}

print(dict)

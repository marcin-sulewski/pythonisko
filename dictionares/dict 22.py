dict = {'a': 10, 'b': 30, 'c': 20, 'd': 40, 'e': 50}

highest_values = sorted(dict.items(), key=lambda x: x[1], reverse=True)[:3]

print("najwieksze 3 wartosci: ")
for key, value in highest_values:
    print(key, ":", value)

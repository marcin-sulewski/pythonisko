x = 'w3resource'

char_count = {}

for char in x:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)

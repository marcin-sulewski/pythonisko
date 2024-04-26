text = input("Wpisz zdanie: ")

words = text.split()

reversed_words = words[::-1]

reversed_string = ' '.join(reversed_words)

print("Zdanie napisane odwrotnie: ", reversed_string)

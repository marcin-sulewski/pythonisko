lista = input("Wpisz liste: ").split()

count = 0
for string in lista:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print(count)

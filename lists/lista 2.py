lista = [int(item) for item in input("Wpisz liste oddzielona spacja: ").split()]
iloczyn = 1

for item in lista:
    iloczyn *= item

print(iloczyn)

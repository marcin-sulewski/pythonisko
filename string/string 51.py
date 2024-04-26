word = input("Wpisz coś")

znak_count = {}


for znak in word:
    if znak in znak_count:
        znak_count[znak] += 1
    else:
        znak_count[znak] = 1


for znak in word:
    if znak_count[znak] == 1:
        print("Pierwszy niepowtarzający się znak to: ", znak)
        break
else:
    print("Nie znaleziono potwarzających się znaków.")

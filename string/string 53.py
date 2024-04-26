word = input("Wpisz cos: ")

seen = set()

for znak in word:
    if znak in seen:
        print("Pierwszy powtarzający sie znak to:", znak)
        break
    else:
        seen.add(znak)
else:
    print("Zaden znak sie nie powtarza.")

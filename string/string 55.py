word = input("Wpisz cos: ")

seen = set()

words = word.split()

for word in words:
    if word in seen:
        print("Pierwsze powtarzajace sie slowo to: ", word)
        break
    else:
        seen.add(word)
else:
    print("Nie ma powtarzajacych sie slow.")

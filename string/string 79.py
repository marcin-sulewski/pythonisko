word = input("Wpisz cos: ")

words = word.split()

smallest_word = None
largest_word = None

for word in words:
    if smallest_word is None or len(word) < len(smallest_word):
        smallest_word = word
    
    if largest_word is None or len(word) > len(largest_word):
        largest_word = word

if smallest_word and largest_word:
    print("Najkrótsze słowo to: ", smallest_word)
    print("Najwieksze słowo to: ", largest_word)
else:

    print("Nie znaleziono słów w wpisanej treści.")
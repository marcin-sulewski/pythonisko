word = input("Wpisz kilka słow: ")

words = word.split()

s_words = sorted(words, key=lambda word: word[0])
s_string = ' '.join(s_words)

print("Posortowane według pierwszej litery: ", s_string)

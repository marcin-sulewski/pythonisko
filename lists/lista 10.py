lista = ["apple", "banana", "orange", "grape", "kiwi"]
n = int(input("Enter the minimum length of words to consider: "))

long_words = [word for word in lista if len(word) > n]
print("slowa dluzsze niz ", n, " : ", long_words)

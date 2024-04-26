import string

word = input("Wpisz cos ze znakami interpunkcyjnymi: ")

punctuation_chars = string.punctuation

result_text = ''.join(char for char in word if char not in punctuation_chars)

print("Wpisany text: ")
print(word)

print("Bez znaków interpukcyjnych: ")
print(result_text)

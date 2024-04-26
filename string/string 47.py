word = input("Wpisz coś: ")
n = int(input("Wpisz ilość znaków które mają zostać, sprowadzone do małej litery: "))

lowercased_word = word[:n].lower() + word[n:]
print("Zaczynając od pierwszych", n, "znaków: ", lowercased_word)

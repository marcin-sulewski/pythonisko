word = input("Wpisz cos: ")

sum = 0

for znak in word:

    if znak.isdigit():

        sum += int(znak)

print("Suma wszystkich cyfr w: " + word + " to: ", sum)

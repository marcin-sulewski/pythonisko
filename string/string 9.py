word = input("Podaj słowo ")
index = int(input("Podaj index znaku który chesz usunąć: "))

if 0 <= index < len(word):
    result = word[:index] + word[index+1:]
    print(result)
else:
    print("Zły index")

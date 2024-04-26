word = input("Podaj słowo: ")

if len(word) < 2:
    result = ""
else:
    result = word[:2] + word[-2:]

print(result)

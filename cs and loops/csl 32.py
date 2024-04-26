letter = input("Input a letter of the alphabet: ").lower()

if len(letter) == 1 and letter.isalpha():
    if letter in 'aeiou':
        print(letter, "is a vowel.")
    else:
        print(letter, "is a consonant.")
else:
    print("Invalid input.")

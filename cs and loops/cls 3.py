import random

target_number = random.randint(1, 9)

correct_guess = False

while not correct_guess:
    guess = int(input("zgadnij liczbe od 1 do 9 "))

    if guess == target_number:
        print("ladnie")
        correct_guess = True
    else:
        print("sproboj jeszcze raz")

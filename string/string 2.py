word = input("Podaj słowo ")
fq = {}

for znak in word:
    if znak in fq:
        fq[znak] += 1
    else:
        fq[znak] = 1

print("W twoim słowie jest tyle poszczególnych znaków", fq)

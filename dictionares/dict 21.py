from itertools import product

dict = {'1': ['a', 'b'], '2': ['c', 'd']}

combinations = [''.join(comb) for comb in product(*dict.values())]

for combination in combinations:
    print(combination)

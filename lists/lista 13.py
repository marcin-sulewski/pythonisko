depth = 3
rows = 4
cols = 6

lista = [[['*' for _ in range(cols)] for _ in range(rows)] for _ in range(depth)]

for i in range(depth):
    print(f"Layer {i+1}:")
    for j in range(rows):
        print(' '.join(lista[i][j]))
    print()

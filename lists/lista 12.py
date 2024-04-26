lista = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
indices_to_remove = [0, 4, 5]

result_list = [lista[i] for i in range(len(lista)) if i not in indices_to_remove]

print("Resulting list after removal:", result_list)

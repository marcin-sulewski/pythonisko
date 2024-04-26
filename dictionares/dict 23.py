from collections import Counter

dict = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

combined_values = Counter()

for d in dict:
    combined_values[d['item']] += d['amount']

print(combined_values)

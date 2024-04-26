dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

all_values = [value for d in dict for value in d.values()]


unique_values = set(all_values)

print(unique_values)

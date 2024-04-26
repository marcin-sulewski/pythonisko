m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

two_dimensional_array = [[i * j for j in range(n)] for i in range(m)]

print("Two-dimensional array:")
for row in two_dimensional_array:
    print(row)

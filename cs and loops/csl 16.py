result = []

for num in range(100, 401):
    digits = [int(digit) for digit in str(num)]
    if all(digit % 2 == 0 for digit in digits):
        result.append(str(num))

print(",".join(result))

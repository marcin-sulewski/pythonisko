binary_numbers = input("Enter comma separated 4-digit binary numbers: ").split(',')

divisible_by_5 = [num for num in binary_numbers if int(num, 2) % 5 == 0]

print("Numbers divisible by 5:", ','.join(divisible_by_5))

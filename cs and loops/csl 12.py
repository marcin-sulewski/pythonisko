print("Enter lines (enter a blank line to terminate):")
lines = []

while True:
    line = input()
    if line:
        lines.append(line.lower())
    else:
        break

print("Output:")
for line in lines:
    print(line)

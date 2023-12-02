import numpy as np

with open('ex1/data.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Remove newline characters from each line
lines = [line.strip() for line in lines]

# Print the result or use it as needed
result = []
for line in lines:
    digits = [char for char in line if char.isdigit()]
    if digits:
        first_last_digits = digits[0] + digits[-1]
        result.append(int(first_last_digits))

print(np.sum(result))

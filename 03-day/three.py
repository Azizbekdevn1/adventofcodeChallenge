# One part
import re


def parse_and_calculate(memory):
    # Regex pattern to match valid mul(X,Y) instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Find all matches in the memory string
    matches = re.findall(pattern, memory)

    # Calculate the sum of the results
    total = sum(int(x) * int(y) for x, y in matches)

    return total


# Read corrupted memory input from input.txt
with open('input.txt', 'r') as file:
    memory = file.read()

# Calculate the result
result = parse_and_calculate(memory)

# Print the result
print("The sum of all valid mul(X,Y) results is:", result)

#Two part
def parse_and_calculate_two(memory):
    # Regex patterns to match instructions
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Split the memory into tokens to process sequentially
    tokens = re.split(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', memory)

    total = 0
    enabled = True  # Initially, mul instructions are enabled

    for token in tokens:
        token = token.strip()

        if re.fullmatch(do_pattern, token):
            enabled = True  # Enable future mul instructions
        elif re.fullmatch(dont_pattern, token):
            enabled = False  # Disable future mul instructions
        elif re.fullmatch(mul_pattern, token) and enabled:
            # Extract numbers and calculate multiplication
            x, y = map(int, re.findall(r"\d+", token))
            total += x * y

    return total

# Read corrupted memory input from input.txt
with open('input.txt', 'r') as file:
    memory = file.read()

# Calculate the result
result = parse_and_calculate_two(memory)

# Print the result
print("The sum of all valid mul(X,Y) results is:", result)

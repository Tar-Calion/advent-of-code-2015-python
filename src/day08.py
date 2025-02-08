import re

def count_string_literals(input_string):
    lines = [line.strip() for line in input_string.splitlines()]

    total_characters = sum(len(line) for line in lines)
    memory_characters = sum(calculate_memory_characters(line) for line in lines)

    return total_characters - memory_characters

def calculate_memory_characters(line):
    # Remove outer quotes
    processed = line[1:-1]
    # Replace escaped backslashes and quotes
    processed = re.sub(r'\\\\', r'\\', processed)
    processed = re.sub(r'\\"', r'"', processed)
    # Replace hex escapes with single character
    processed = re.sub(r'\\x[0-9a-fA-F]{2}', 'X', processed)
    return len(processed)

def main():
    with open("data/day08/input.txt", "r") as file:
        input_string = file.read()
    result = count_string_literals(input_string)
    print(result)

if __name__ == "__main__":
    main()






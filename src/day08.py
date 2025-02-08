import re

def count_escapes(lines):
    total_characters = sum(len(line) for line in lines)
    memory_characters = sum(calculate_memory_characters(line) for line in lines)
    return total_characters - memory_characters

def calculate_memory_characters(line):
    # Remove outer quotes
    processed = line[1:-1]
    # Replace escaped backslashes and quotes
    processed = re.sub(r'\\\\', r'X', processed)
    processed = re.sub(r'\\"', r'"', processed)
    # Replace hex escapes with single character
    processed = re.sub(r'\\x[0-9a-fA-F]{2}', 'X', processed)
    return len(processed)

def encode_string_representation(line):
    # Escape backslashes and double quotes
    encoded = line.replace('\\', '\\\\').replace('"', '\\"')
    # Enclose in double quotes
    return f'"{encoded}"'

def main():
    with open("data/day08/input.txt", "r") as file:
        input_string = file.read()
    lines = [line.strip() for line in input_string.splitlines()]
    result = count_escapes(lines)
    print("Original:", result)

    encoded_lines = [encode_string_representation(line) for line in lines]
    result = count_escapes(encoded_lines)
    print("Encoded:", result)

if __name__ == "__main__":
    main()






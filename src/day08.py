import re

def count_escapes(input_string):
    lines = [line.strip() for line in input_string.splitlines()]

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
    result = count_escapes(input_string)
    print("Original:", result)

    encoded_lines = [encode_string_representation(line.strip()) for line in input_string.splitlines()]
    encoded_string = '\n'.join(encoded_lines)
    result = count_escapes(encoded_string)
    print("Encoded:", result)


if __name__ == "__main__":
    main()






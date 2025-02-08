import re

def count_string_literals(input_string):
    lines = [line.strip() for line in input_string.splitlines()]

    total_characters = sum(len(line) for line in lines)
    memory_characters = 0

    for line in lines:
        # Remove outer quotes
        processed = line[1:-1]
        # Replace escaped characters
        memory_characters += processed.count('\\\\')
        processed = processed.replace('\\\\', '')
        memory_characters += processed.count('\\"')
        processed = processed.replace('\\"', '')
        # Replace hex escapes with single character
        matches = re.findall(r'\\x[0-9a-f]{2}', processed)
        memory_characters += len(matches)

        processed = re.sub(r'\\x[0-9a-f]{2}', '', processed)
        print(processed)
        memory_characters += len(processed)

    print("Total", total_characters)
    print("Memory", memory_characters)
    return total_characters - memory_characters

def main():
    with open("data/day08/input.txt", "r") as file:
        input_string = file.read()
    result = count_string_literals(input_string)
    print(result)

if __name__ == "__main__":
    main()






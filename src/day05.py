import re


def has_three_vowels(line: str):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for vowel in vowels:
        vowel_count = vowel_count + line.count(vowel)
    return vowel_count >= 3


def has_double_letter(line):
    return re.search(r"(.)\1", line) is not None


def has_no_evil_strings(line):
    evil_strings = ["ab", "cd", "pq", "xy"]
    for evil_string in evil_strings:
        if evil_string in line:
            return False
    return True


def has_double_pair(line):
    return re.search(r"(\w\w).*\1", line) is not None


def has_sandwich(line):
    return re.search(r"(\w).\1", line) is not None


def is_nice(line):
    return (
        has_three_vowels(line) and has_double_letter(line) and has_no_evil_strings(line)
    )


def is_nice_new_rules(line):
    return has_double_pair(line) and has_sandwich(line)


def count_nice():
    with open("data/day05/input.txt", mode="r", encoding="utf-8") as file:
        nice_count = 0
        for line in file:
            if is_nice(line):
                nice_count = nice_count + 1

        print(nice_count)


def count_nice_new_rules():
    with open("data/day05/input.txt", mode="r", encoding="utf-8") as file:
        nice_count = 0
        for line in file:
            if is_nice_new_rules(line):
                nice_count = nice_count + 1

        print(nice_count)


count_nice()
count_nice_new_rules()

import data
import re


def disassemble(line):
    pattern = r"(\d+)-(\d+) (\w): (.+)"
    match = re.match(pattern, line)
    groups = match.groups()
    return groups


def part_one(data):

    valid_count = 0
    invalid_count = 0

    for line in data:

        sc_min, sc_max, special_character, password = disassemble(line)

        count = password.count(special_character)
        rule = range(int(sc_min), int(sc_max) + 1)

        if count in rule:
            valid_count += 1
        else:
            invalid_count += 1

    print(f"Valid:   {valid_count}")
    print(f"Invalid: {invalid_count}")

    return valid_count


def part_two(data):

    valid_count = 0
    invalid_count = 0

    for line in data:

        index_one, index_two, special_character, password = disassemble(line)
    
        index_one_match = password[int(index_one) - 1] == special_character
        index_two_match = password[int(index_two) - 1] == special_character
        valid_password = index_one_match ^ index_two_match

        if valid_password:
            valid_count += 1
        else:
            invalid_count += 1

    print(f"Valid:   {valid_count}")
    print(f"Invalid: {invalid_count}")

    return valid_count


if __name__ == "__main__":

    input_data = data.load_lines("data/day02.txt")
    
    print("==== Part 1 ====")
    part_one(input_data)

    print("==== Part 2 ====")
    part_two(input_data)


import data
from time import sleep


def part_one(filename: str):
    lines = data.load_lines(filename)
    index, accumulator = process_lines(lines)
    print(accumulator)
    return accumulator


def part_two(filename: str):

    lines = data.load_lines(filename)

    for i in range(len(lines)):

        copy = lines.copy()

        if copy[i].startswith("jmp"):
            copy[i] = copy[i].replace("jmp", "nop")
        elif copy[i].startswith("nop"):
            copy[i] = copy[i].replace("nop", "jmp")

        index, accumulator = 0, 0
        seen = []

        while True:

            if index == len(lines):
                print(accumulator)
                return accumulator

            elif index in seen:
                break

            else:
                seen.append(index)
                index, accumulator = process_instruction(copy[index], index, accumulator)


def process_instruction(instruction: str, index: int, accumulator: int):

    operation, argument = instruction.split(" ")

    if operation == "acc":
        accumulator += int(argument)
        index += 1
    elif operation == "jmp":
        offset = int(argument)
        index += offset
    elif operation == "nop":
        index += 1
    else:
        raise ValueError

    return index, accumulator


def process_lines(lines: list):

    index, accumulator = 0, 0
    seen = []

    while index not in seen:
        seen.append(index)
        index, accumulator = process_instruction(lines[index], index, accumulator)

    return index, accumulator


if __name__ == "__main__":

    print("==== Part 1 ====")
    part_one("data/day08.txt")

    print("==== Part 2 ====")
    part_two("data/day08.txt")


import data
import itertools


def part_one(data):
    result = int()
    data = list(map(lambda x: int(x), data))
    combinations = itertools.combinations(data, 2)
    for combo in combinations:
        added = sum(combo)
        if added == 2020:
            multiplied = combo[0] * combo[1]
            print(f"Combo: {combo}")
            print(f"Multiplied: {multiplied}\n")
            result = multiplied
    return result


def part_two(data):
    result = int()
    data = list(map(lambda x: int(x), data))
    combinations = itertools.combinations(data, 3)
    for combo in combinations:
        added = sum(combo)
        if added == 2020:
            multiplied = combo[0] * combo[1] * combo[2]
            print(f"Combo: {combo}")
            print(f"Multiplied: {multiplied}\n")
            result = multiplied
    return result


if __name__ == "__main__":

    input_data = data.load_lines("data/day01.txt")

    print("==== Part 1 ====")
    part_one(input_data)

    print("==== Part 2 ====")
    part_two(input_data)


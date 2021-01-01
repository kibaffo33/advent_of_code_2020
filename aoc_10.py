import data
import itertools
import multiprocessing
from time import sleep #TODO remove


def prep_data(filename: str):
    lines = data.load_lines(filename)
    lines = list(map(lambda x: int(x), lines))
    return lines


def part_one(filename: str):

    adaptors = prep_data(filename)
    adaptors.sort()

    current_adaptor = 0
    highest_jolt = max(adaptors) + 3

    adaptor_chain = [current_adaptor]
    differences = {1: 0, 2: 0, 3:0}

    while True:
        
        current_adaptor = adaptors.pop(0)
        last_adaptor = adaptor_chain[-1]

        difference = current_adaptor - last_adaptor
        differences[difference] += 1
        assert difference <= 3

        adaptor_chain.append(current_adaptor)

        if current_adaptor >= highest_jolt - 3:

            difference = highest_jolt - current_adaptor
            differences[difference] += 1
            break

    result = differences[1] * differences[3]
    print(result)
    return result


def part_two(filename: str):

    adaptors = prep_data(filename)
    adaptors.append(0)
    adaptors.append(max(adaptors) + 3)
    adaptors.sort()
    
    chain = [0] * (max(adaptors) + 1)
    chain[0] = 1

    for index in range(1, max(adaptors) + 1):
        for x in range(1, 4):
            if (index - x) in adaptors:
                chain[index] += chain[index - x]

    result = chain[-1]
    print(result)
    return result


if __name__ == "__main__":

    print("==== Part 1 ====")
    part_one("data/day10.txt")

    print("==== Part 2 ====")
    part_two("data/day10.txt")


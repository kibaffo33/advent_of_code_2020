import data
from itertools import combinations


def prep_data(filename: str):
    lines = data.load_lines(filename)
    lines = list(map(lambda x: int(x), lines))
    return lines
    
def pointer(lines: list, tail_length: int):

    for index in range(len(lines)):

        if index < tail_length:
            pass
        else:
            head = lines[index]
            tail = lines[index - tail_length:index]
            
            combos = combinations(tail, 2)
            if any(list(map(lambda x: x[0] + x[1] == head, combos))):
                pass
            else:
                return head


def part_one(filename: str, tail_length: int):
    lines = prep_data(filename)
    result = pointer(lines, tail_length)
    print(result)
    return result


def part_two(filename: str, target: int):

    data = prep_data(filename)

    pointer = 0
    size_of_contiguous_set = 2
    sum_of_contiguous_set = 0

    contiguous_set = data[pointer : pointer + size_of_contiguous_set]
    while sum(contiguous_set) != target:
        pointer += 1
        contiguous_set = data[pointer : pointer + size_of_contiguous_set]
        if pointer > len(data) - size_of_contiguous_set - 1:
            pointer = 0
            size_of_contiguous_set += 1
        if size_of_contiguous_set > len(data) // 2:
            print("Broken")
            break

    print("Size of set:", size_of_contiguous_set)
    print("Set:", contiguous_set)
    print("Sum of set:", sum(contiguous_set))
    smallest = min(contiguous_set)
    largest = max(contiguous_set)
    print("Smallest:", smallest)
    print("Largest:", largest)

    result = smallest + largest
    print("Result:", result)

    return result


if __name__ == "__main__":

    print("==== Part 1 ====")
    part_one_result = part_one("data/day09.txt", 25)

    print("==== Part 2 ====")
    part_two("data/day09.txt", part_one_result)


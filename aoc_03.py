import data
import math


def descend(x_rate: int, y_rate: int, course: list) -> int:

    x, y = 0, 0
    hits, misses = 0, 0

    height = len(course)
    width = len(course[0])

    while y < height:

        x_position = x % width
        current_position = course[y][x_position]

        if current_position == "#":
            hits += 1
        else:
            misses += 1

        # Move
        x += x_rate
        y += y_rate

    return hits


def part_one(input_data):

    
    hits = descend(3, 1, input_data)

    print(f"Hits: {hits}")

    return hits


def part_two(input_data):

    rates = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    hits = list(map(lambda rate: descend(rate[0], rate[1], input_data), rates))

    result = math.prod(hits)

    print(f"Result: {result}")


    return result
    

if __name__ == "__main__":

    input_data = data.load_lines("data/day03.txt")

    print("==== Part 1 ====")
    part_one(input_data)

    print("==== Part 2 ====")
    part_two(input_data)


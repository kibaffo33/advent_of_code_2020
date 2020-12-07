import data


def get_row_number(boarding_pass: str):
    seats = list(range(128))
    for character in boarding_pass[:7]:
        split = len(seats) // 2
        if character == "F":
            seats = seats[:split]
        elif character == "B":
            seats = seats[split:]
    return seats[0]


def get_col_number(boarding_pass: str):
    seats = list(range(8))
    for character in boarding_pass[7:]:
        split = len(seats) // 2
        if character == "R":
            seats = seats[split:]
        elif character == "L":
            seats = seats[:split]
    return seats[0]


def get_seat(boarding_pass: str):
    row = get_row_number(boarding_pass)
    col = get_col_number(boarding_pass)
    return (row, col)


def get_seat_id(boarding_pass: str):
    row, col = get_seat(boarding_pass)
    seat_id = row * 8 + col
    return seat_id


def part_one(input_data):
    seat_ids = list(map(lambda x: get_seat_id(x), input_data))
    highest = max(seat_ids)
    print(highest)
    return highest


def part_two(input_data):
    taken_seats = list(map(lambda x: get_seat(x), input_data))
    taken_seats.sort()

    possible_seats = list(map(lambda x: f"{x:02o}", range(128 * 8)))
    possible_seats = list(map(lambda x: (int(x[:-1]), int(x[-1])), possible_seats))
    while possible_seats[0] < taken_seats[0]:
        possible_seats.pop(0)
    while possible_seats[-1] > taken_seats[-1]:
        possible_seats.pop(-1)

    result = None
    possible_results = list(filter(lambda x: x not in taken_seats, possible_seats))
    assert len(possible_results) == 1
    row, col = possible_results[0]
    result = row * 8 + col
    print(result)
    return result


if __name__ == "__main__":

    input_data = data.load_lines("data/day05.txt")
    
    print("==== Part 1 ====")
    part_one(input_data)

    print("==== Part 2 ====")
    part_two(input_data)



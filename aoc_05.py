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


if __name__ == "__main__":

    input_data = data.load_lines("data/day05.txt")
    print(input_data)
    
    print("==== Part 1 ====")
    part_one(input_data)

    #print("==== Part 2 ====")
    #part_two(input_data)



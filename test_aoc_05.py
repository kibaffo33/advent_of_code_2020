import aoc_05


def test_get_row_number():

    # GIVEN sample boarding pass
    boarding_pass = "FBFBBFFRLR"

    # WHEN calling get_row_number(...)
    result = aoc_05.get_row_number(boarding_pass)

    # THEN result should be 44
    assert result == 44


def test_get_col_number():

    # GIVEN sample boarding pass
    boarding_pass = "FBFBBFFRLR"

    # WHEN calling get_col_number(...)
    result = aoc_05.get_col_number(boarding_pass)

    # THEN result should be 5
    assert result == 5


def test_get_seat():

    # GIVEN sample boarding pass
    boarding_pass = "FBFBBFFRLR"

    # WHEN calling get_col_number(...)
    result = aoc_05.get_seat(boarding_pass)

    # THEN result should be 5
    assert result == (44, 5)
    

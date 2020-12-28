import aoc_09


def test_part_one():

    # GIVEN sample data
    sample_data = "data/day09_sample.txt"

    # WHEN calling part_one(...)
    result = aoc_09.part_one(sample_data, 5)

    # THEN result should be 4
    assert result == 127


def test_part_two():

    # GIVEN sample data
    sample_data = "data/day09_sample.txt"

    # WHEN calling part_one(...)
    result = aoc_09.part_two(sample_data, 127)

    # THEN result should be 4
    assert result == 62


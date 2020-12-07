import aoc_06


def test_part_one():

    # GIVEN sample data
    sample_data = "data/day06_sample.txt"

    # WHEN calling part_one(...)
    result = aoc_06.part_one(sample_data)

    # THEN result should be 11'
    assert result == 11


def test_part_two():

    # GIVEN sample data
    sample_data = "data/day06_sample.txt"

    # WHEN calling part_one(...)
    result = aoc_06.part_two(sample_data)

    # THEN result should be 11'
    assert result == 6


import aoc_10


def test_part_one():

    # GIVEN sample data
    sample_data = "data/day10_sample2.txt"

    # WHEN calling part_one(...)
    result = aoc_10.part_one(sample_data)

    # THEN result should be 4
    assert result == 22 * 10


def test_part_two():

    # GIVEN sample data
    sample_data = "data/day10_sample2.txt"

    # WHEN calling part_one(...)
    result = aoc_10.part_two(sample_data)

    # THEN result should be 4
    assert result == 19208


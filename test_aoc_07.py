import aoc_07


def test_part_one():

    # GIVEN sample data
    sample_data = "data/day07_sample.txt"

    # WHEN calling part_one(...)
    result = aoc_07.part_one(sample_data)

    # THEN result should be 4
    assert result == 4


import aoc_08



def test_part_one():

    # GIVEN sample data
    sample_data = "data/day08_sample.txt"

    # WHEN calling part_one(...)
    result = aoc_08.part_one(sample_data)

    # THEN result should be 4
    assert result == 5


def test_part_two():

    # GIVEN sample data
    sample_data = "data/day08_sample.txt"

    # WHEN calling part_one(...)
    result = aoc_08.part_two(sample_data)

    # THEN result should be 4
    assert result == 8

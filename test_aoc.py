import data
import aoc_01, aoc_02, aoc_03, aoc_04


def test_aoc_01_part_one():
    
    # GIVEN input data
    input_data = data.load_lines("data/day01.txt")

    # WHEN calling part_one()
    result = aoc_01.part_one(input_data)

    # THEN result is correct
    assert result == 989824


def test_aoc_01_part_two():
    
    # GIVEN input data
    input_data = data.load_lines("data/day01.txt")

    # WHEN calling part_two()
    result = aoc_01.part_two(input_data)

    # THEN result is correct
    assert result == 66432240


def test_aoc_02_part_one():

    # GIVEN input data
    input_data = data.load_lines("data/day02.txt")

    # WHEN calling part_one()
    result = aoc_02.part_one(input_data)

    # THEN result is correct
    assert result == 556


def test_aoc_02_part_two():

    # GIVEN input data
    input_data = data.load_lines("data/day02.txt")

    # WHEN calling part_one()
    result = aoc_02.part_two(input_data)

    # THEN result is correct
    assert result == 605


def test_aoc_03_part_one():

    # GIVEN input data
    input_data = data.load_lines("data/day03.txt")

    # WHEN calling part_one()
    result = aoc_03.part_one(input_data)

    # THEN result is correct
    assert result == 211


def test_aoc_03_part_two():

    # GIVEN input data
    input_data = data.load_lines("data/day03.txt")

    # WHEN calling part_one()
    result = aoc_03.part_two(input_data)

    # THEN result is correct
    assert result == 3584591857


def test_aoc_04_part_one():

    # GIVEN input data
    # WHEN calling part_one()
    result = aoc_04.part_one()

    # THEN result is correct
    assert result == 219


def test_aoc_04_part_two():

    # GIVEN input data
    # WHEN calling part_two()
    result = aoc_04.part_two()

    # THEN result is correct
    assert isinstance(result, int)




def test_aoc_04_part_one():

    # GIVEN input data
    # WHEN calling part_one()
    result = aoc_04.part_one()

    # THEN result is correct
    assert result == 219



def test_aoc_04_part_two():

    # GIVEN input data
    # WHEN calling part_two()
    result = aoc_04.part_two()

    # THEN result is correct
    assert result == 127



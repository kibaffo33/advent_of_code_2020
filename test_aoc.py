import data
import aoc_01, aoc_02, aoc_03, aoc_04, aoc_05, aoc_06, aoc_07, aoc_08


"""Day 01"""

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


"""Day 02"""

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


"""Day 03"""

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


"""Day 04"""

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


"""Day 05"""

def test_aoc_05_part_one():

    # GIVEN input data
    input_data = data.load_lines("data/day05.txt")

    # WHEN calling part_one()
    result = aoc_05.part_one(input_data)

    # THEN result is correct
    assert result == 842


def test_aoc_05_part_two():

    # GIVEN input data
    input_data = data.load_lines("data/day05.txt")

    # WHEN calling part_two()
    result = aoc_05.part_two(input_data)

    # THEN result is correct
    assert result == 617


"""Day 06"""

def test_aoc_06_part_one():

    # GIVEN input data
    input_data = "data/day06.txt"

    # WHEN calling part_one()
    result = aoc_06.part_one(input_data)

    # THEN result is correct
    assert result == 6549


def test_aoc_06_part_two():

    # GIVEN input data
    input_data = "data/day06.txt"

    # WHEN calling part_one()
    result = aoc_06.part_two(input_data)

    # THEN result is correct
    assert result == 3466


"""Day 07"""

def test_aoc_07_part_one():

    # GIVEN input data
    input_data = "data/day07.txt"

    # WHEN calling part_one()
    result = aoc_07.part_one(input_data)

    # THEN result is correct
    assert result == 226


def test_aoc_07_part_two():

    # GIVEN input data
    input_data = "data/day07.txt"

    # WHEN calling part_one()
    result = aoc_07.part_two(input_data)

    # THEN result is correct
    assert result == 9569


"""Day 08"""

def test_aoc_08_part_one():

    # GIVEN input data
    input_data = "data/day08.txt"

    # WHEN calling part_one()
    result = aoc_08.part_one(input_data)

    # THEN result is correct
    assert result == 1317


def test_aoc_08_part_two():

    # GIVEN input data
    input_data = "data/day08.txt"

    # WHEN calling part_two()
    result = aoc_08.part_two(input_data)

    # THEN result is correct
    assert result == 1033


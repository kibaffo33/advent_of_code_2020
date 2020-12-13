import data
import re
from dataclasses import dataclass


def part_one(filename: str):

    answer = set()

    rules = create_rule_dict(filename)

    def search(outer_colour, colour):
        if "shiny gold" in rules[colour]:
            answer.add(outer_colour)
        for inner_colour in set(rules[colour]):
            search(outer_colour, inner_colour)

    for bag in rules:
        search(bag, bag)

    answer = len(answer)

    print(answer)
    return answer


def part_two(filename: str):

    rules = create_rule_dict(filename)

    @dataclass
    class Count:
        count: int

    count = Count(0)

    def count_contents(colour):
        bag_conents = len(rules[colour])
        count.count += bag_conents

        for bag in rules[colour]:
            count_contents(bag)
        
    count_contents("shiny gold")

    count = count.count

    print(count)
    
    return count


def process_rule(line: str):

    # Split rule into bag colour and contents
    pattern = r"(.+) bags contain (.+)"
    match = re.match(pattern, line)
    groups = match.groups()
    colour = groups[0]
    contents = groups[1]

    # Seperate contents into a list
    contents = contents[:-1].split(", ")
    contents = list(map(lambda x: x.replace(" bags", ""), contents))
    contents = list(map(lambda x: x.replace(" bag", ""), contents))

    # Process the contents list
    bag = {colour: []}
    
    for item in contents:
        pattern = r"(\d+) (.+)"
        match = re.fullmatch(pattern, item)
        if match:
            groups = match.groups()
            quantity = groups[0]
            color = groups[1]

            for number in range(int(quantity)):
                bag[colour].append(color)
    
    # Return a Bag dataclass
    return bag



def create_rule_dict(filename: str):
    lines = data.load_lines(filename)
    rules = {}
    for line in lines:
        rules.update(process_rule(line))
    return rules


if __name__ == "__main__":

    print("==== Part 1 ====")
    part_one("data/day07.txt")

    print("==== Part 2 ====")
    part_two("data/day07.txt")

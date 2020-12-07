import data


def part_one(filename: str):
    result = 0
    groups = load_groups(filename)
    for group in groups:
        unique_letters = get_unique_letters(group)
        score = len(unique_letters)
        result += score
    print(result)
    return result


def part_two(filename: str):
    groups = load_groups(filename)
    score = 0
    for group in groups:
        unique_letters = get_unique_letters(group)
        for letter in unique_letters:
            individual_answers = get_individual_answers(group)
            answers_have_letter = list(map(lambda answer: letter in answer, individual_answers))
            common_answer = all(answers_have_letter)
            if common_answer:
                score += 1
    print(score)
    return score


def load_groups(filename: str):
    forms_batch = data.load_data(filename)
    groups = forms_batch.split("\n\n")
    groups[-1] = groups[-1].rstrip()
    return groups

def get_unique_letters(group: str):
    group = group.replace("\n", "")
    unique_letters = list(set(group))
    return unique_letters

def get_individual_answers(group: str):
    individual_answers = group.split("\n")
    return individual_answers


if __name__ == "__main__":

    print("==== Part 1 ====")
    part_one("data/day06.txt")

    print("==== Part 2 ====")
    part_two("data/day06.txt")



def load_lines(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.rstrip(), lines))
    return lines


def load_data():
    with open(filename, "r") as file:
        data = file.read()
    return data


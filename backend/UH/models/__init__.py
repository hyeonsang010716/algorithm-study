from .graph import p1167, p1967
from typing import List


def get_answer(number: int, input: List):
    name = f"p{number}"
    if name == "p1167":
        return p1167.get_answer(input)
    elif name == "p1967":
        return p1967.get_answer(input)
    else:
        return None


if __name__ == "__main__":
    input_list = ['5\n1 3 2 -1\n2 4 4 -1\n3 1 2 4 3 -1\n4 2 4 3 3 5 6 -1\n5 4 6 -1']
    print(get_answer(1167, input_list))
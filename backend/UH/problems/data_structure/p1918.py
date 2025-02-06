from collections import deque
from typing import List


priority = {
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1
}

def change_postfix(arr: List[str]) -> List[str]:
    stack = deque()
    result = deque()

    for curr in arr:
        if curr == ")":
            while True:
                tmp = stack.pop()
                if tmp == "(":
                    break
                result.append(tmp)
        elif curr == "(":
            stack.append(curr)
        elif curr in priority.keys():
            while stack and stack[-1] != "(" and priority[stack[-1]] >= priority[curr]:
                result.append(stack.pop())
            stack.append(curr)
        else:
            result.append(curr)
    while stack:
        result.append(stack.pop())
    return "".join(result)


def process_input_data(input_data: str) -> List[str]:
    return list(input_data)


def solution(input_data: str) -> str:
    return change_postfix(process_input_data(input_data))


if __name__ == "__main__":
    string = "A+B*C-D/E"
    print(solution(string))

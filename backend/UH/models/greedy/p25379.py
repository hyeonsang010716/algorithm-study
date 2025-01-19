from typing import List, Tuple


def count_odd(arr: List[int]) -> int:
    left_cnt = right_cnt = 0
    left_result = right_result = 0

    for i in arr:
        if not is_odd(i):
            left_cnt += 1
            right_result += right_cnt
        else:
            right_cnt += 1
            left_result += left_cnt
    return min(right_result, left_result)


def is_odd(num: int) -> bool:
    return True if num%2 != 0 else False


def process_input_data(input_data: str) -> Tuple[int, int]:
    input_li = list(map(int, input_data.split()))
    return input_li[0], input_li[1:]


def solution(input_data: str):
    _, arr = process_input_data(input_data)
    return count_odd(arr)


if __name__ == "__main__":
    inputs = '4\n4 5 1 0'
    print(solution(inputs))

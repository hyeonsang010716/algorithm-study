from typing import List


def gcd(num1: int, num2: int) -> int:
    up, low = max(num1, num2), min(num1, num2)
    if up%low == 0:
        return low
    return gcd(low, up%low)


def lcm(num1: int, num2: int) -> int:
    return num1*num2 // gcd(num1, num2)


def process_input_data(input_data: str):
    input_list = list(map(int, input_data.split()))
    n = input_list[0]
    arr = input_list[1:]
    return n, arr


def solution(input_data: str):
    _, arr = process_input_data(input_data)
    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)

    return result


if __name__ == "__main__":
    input_list = '5\n1 2 3'
    print(solution(input_list))
def process_input_data(input_data: str) -> int:
    return int(input_data)

def solution(input_data: str):
    n = process_input_data(input_data)
    a_cnt, b_cnt = 1, 0

    for _ in range(n):
        a_cnt, b_cnt = b_cnt, a_cnt + b_cnt
    return list(map(str, [a_cnt, b_cnt]))


if __name__ == "__main__":
    n = "10"
    print(solution(n))
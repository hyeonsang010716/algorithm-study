def process_input_data(data: str):
    import sys
    from io import StringIO

    sys.stdin = StringIO(data)



def solution(data: str):
    process_input_data(data)
    n = int(input())
    if n == 1:
        return 666
    cnt = 1
    start = 666
    while True:
        start += 1
        if '666' in (str(start)):
            cnt += 1
            if cnt == n:
                return start


if __name__ == "__main__":
    print(solution("2"))

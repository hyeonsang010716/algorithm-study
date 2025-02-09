def merge_range(point_1, point_2):
    return (max(point_1[0], point_2[0]), min(point_1[1], point_2[1]))


def solution():
    n = int(input())
    curr_range = [[0, float('Inf')] for _ in range(3)]
    result = 1

    for _ in range(n):
        input_range = list(map(int, input().split()))
        for i in range(3):
            curr_range[i] = merge_range(curr_range[i], [input_range[i], input_range[i+3]])

    for li in curr_range:
        if li[1] <= li[0]:
            result *= 0
        else:
            result *= (li[1]-li[0])
    return result


if __name__ == "__main__":
    import sys
    from io import StringIO

    s = """2
1 1 1 3 3 3
2 2 2 3 3 3"""

    sys.stdin = StringIO(s)
    print(solution())
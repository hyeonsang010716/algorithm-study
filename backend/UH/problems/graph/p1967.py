from typing import Dict, Tuple, List

def dfs(start: int, graph: Dict[int, int]) -> Tuple[int, int]:
    if start not in graph:
        return 0, 0

    from collections import deque

    q = deque()
    visit = set([start])

    outer_node = 0
    max_len = 0

    for node, w in graph[start].items():
        q.append((node, w))
        visit.add(node)

    while q:
        curr, wei = q.popleft()
        if max_len < wei:
            max_len = wei
            outer_node = curr

        for nx, nw in graph[curr].items():
            if nx not in visit:
                q.append((nx, wei+nw))
                visit.add(nx)

    return outer_node, max_len


def process_input_data(input_data: str):
    input_list = list(map(int, input_data.split()))

    n = input_list[0]
    graph = {k: {} for k in range(1, n+1)}

    for i in range(1, len(input_list), 3):
        parent, child, weight = input_list[i], input_list[i+1], input_list[i+2]
        graph[parent][child] = weight
        graph[child][parent] = weight
    return n, graph


def solution(input_data: str) -> Tuple[int, Dict[int, int]]:
    _, graph = process_input_data(input_data)
    outer, _ = dfs(1, graph)
    _, result = dfs(outer, graph)
    return result


if __name__ == "__main__":
    li =  '12\n1 2 3\n1 3 2\n2 4 5\n3 5 11\n3 6 9\n4 7 1\n4 8 7\n5 9 15\n5 10 4\n6 11 6\n6 12 10'
    print(solution(li))
    
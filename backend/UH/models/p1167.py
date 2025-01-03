from typing import Dict, List


def solution(n: int, graph: Dict[int, Dict[int, int]]):
    def dfs(start):
        from collections import deque
        width = 0
        
        stack = deque([(start, 0)]) 
        visit = set([start])

        while stack:
            curr, wei = stack.pop()
            if wei > width:
                width = wei
                node = curr

            for nx, nx_wei in graph[curr].items():
                if nx not in visit:
                    stack.append((nx, nx_wei+wei))
                    visit.add(nx)
        return (node, width)
    
    node, _ = dfs(1)
    _, result = dfs(node)

    return result


def get_answer(input_list: List[List[int]]):
    n = input_list[0][0]
    graph = {k: {} for k in range(1, n+1)}

    for tmp in input_list[1:]:
        for _ in range(n):
            start = tmp[0]
            i = 1
            while True:
                node = tmp[i]
                if node == -1:
                    break
                graph[start][node] = tmp[i+1]
                i += 2
    return solution(n, graph)


if __name__ == "__main__":
    input_list = [
        [5],
        [1, 3, 2, -1],
        [2, 4, 4, -1],
        [3, 1, 2, 4, 3, -1],
        [4, 2, 4, 3, 3, 5, 6, -1],
        [5, 4, 6, -1]
    ]

    print(get_answer(input_list))
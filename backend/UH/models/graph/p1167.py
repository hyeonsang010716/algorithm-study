from typing import Dict, List


def get_tree_diameter(n: int, graph: Dict[int, Dict[int, int]]) -> int:
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


def process_input_data(input_data: str):
    arr = list(map(int, input_data.split()))

    n = arr[0]
    graph = {k: {} for k in range(1, n+1)}

    i = 1
    while i < len(arr):
        node = arr[i]
        i += 1
        while arr[i] != -1:
            target = arr[i]
            weight = arr[i+1]
            graph[node][target] = weight
            i += 2
        i += 1
    
    return n, graph


def solution(input_data: str):
    n, graph = process_input_data(input_data)
    return get_tree_diameter(n, graph)


if __name__ == "__main__":
    input_list = '5\n1 3 2 -1\n2 4 4 -1\n3 1 2 4 3 -1\n4 2 4 3 3 5 6 -1\n5 4 6 -1'

    print(solution(input_list))
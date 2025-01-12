import heapq
from typing import List, Dict, Tuple


def dijkstra(graph: Dict[int, List], start: int, length: int):
    '''
    result = []
    

    q 처음 값 - 스타트 기준 갈 수 있는 노드 + 가중치

    q가 빌 때 까지
        현재 가중치 노드 받기
        방문 노드 추가
        반복문 모든 다음 노드 체크
            만약 방문했으면 넘어가기
    '''
    q = []
    result = [float("Inf") for _ in range(length+1)]
    result[start] = 0

    visit = set([start])

    for li in graph[start]:
        wei, i = li[0], li[1]
        heapq.heappush(q, (wei, i))
        result[i] = wei

    while q:
        curr_wei, curr = heapq.heappop(q)
        visit.add(curr)

        for li in graph[curr]:
            nw, nx = li[0], li[1]
            if nw + curr_wei < result[nx] and nx not in visit:
                result[nx] = nw + curr_wei
                heapq.heappush(q, (result[nx], nx))

    return result
    # return result.index(max(result[1:]))


def cmd_input_data() -> Tuple[int, Dict[int, List], int]:
    n, m, x = map(int, input().split())
    graph = {k: [] for k in range(1, n+1)}

    for _ in range(m):
        start, end, weight = map(int, input().split())
        graph[start].append((weight, end))

    return n, graph, x


def process_input_data(input_data: str):
    input_data = list(map(int, input_data.split()))
    n, m, x = input_data[0], input_data[1], input_data[2]
    graph = {k: [] for k in range(1, n+1)}

    for i in range(3, 3*m+1, 3):
        start, end, weight = input_data[i], input_data[i+1], input_data[i+2]
        graph[start].append((weight, end))

    return n, graph, x

def solution(input_data: str):
    length, graph, root = process_input_data(input_data)
    
    result = 0
    back_dist = dijkstra(graph, root, length)
    for i in range(1, length+1):
        go_dist = dijkstra(graph, i, length)[root]
        if go_dist + back_dist[i] > result:
            result = go_dist+back_dist[i]
    return result


if __name__ == "__main__":
    input_str = '4 8 2\r\n1 2 4\r\n1 3 2\r\n1 4 7\r\n2 1 1\r\n2 3 5\r\n3 1 2\r\n3 4 4\r\n4 2 3'
    print(solution(input_str))
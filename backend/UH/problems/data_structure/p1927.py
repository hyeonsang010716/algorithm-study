import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    curr = int(input())
    if curr == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, curr) 
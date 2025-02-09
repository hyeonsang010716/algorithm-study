from collections import deque


n = int(input())
q = deque([i for i in range(1, n+1)])
cnt = 0

while q:
    curr = q.popleft()
    if cnt == 0:
        cnt = 1
    elif cnt == 1:
        q.append(curr)
        cnt = 0

print(curr)

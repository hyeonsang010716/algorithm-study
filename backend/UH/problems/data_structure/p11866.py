from collections import deque


n, k = map(int, input().split())

q = deque([])
cnt = 0
result = []

for i in range(1, n+1):
    q.append(i)

while q:
    curr = q.popleft()
    cnt += 1
    if cnt == k:
        result.append(curr)
        cnt = 0
    else:
        q.append(curr)
print("<", end='')
for i in result[:-1]:
    print(i, end=', ')
print(f"{result[-1]}>", end='')
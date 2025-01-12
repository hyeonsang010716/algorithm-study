
def solve(input):
    sets=input.strip().split('\n\n')
    results=[]
    for set in sets:
        lines = set.strip().split('\n')
        n,m=map(int, lines[0].split())
        arr=[list(map(int, list(line.strip()))) for line in lines[1:]]
        check=min(n,m)
        answer=0
        for i in range(n):
            for j in range(m):
                for k in range(check):
                    if ((i + k) < n) and ((j + k) < m) and (arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]):
                        answer = max(answer, (k + 1)**2)
        results.append(str(answer)+'\n')
    return results

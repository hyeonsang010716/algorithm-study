def solve(Input):
    l = Input.split("\n")
    idx = 1
    answer = ""
    for _ in range(int(l[0])):
        n = int(l[idx])
        idx += 1
        check = dict()

        for i in range(n):
            a , b = map(int,l[idx].split())
            idx += 1
            if a not in check:
                check[a] = {b}
            else:
                check[a].add(b)

        x = True

        y = -1

        for a in check.values():
            if y == -1:
                y = a
            else:
                if y != a:
                    x = False
                    break
                
        if x: answer += "BALANCED" + "\n"
        else: answer += "NOT BALANCED" + "\n"
        
    return answer



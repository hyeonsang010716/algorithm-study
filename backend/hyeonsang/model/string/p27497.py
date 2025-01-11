from collections import deque

def solve(Input):
    input_list = Input.split("\n")
    
    n = int(input_list[0])

    word = deque()

    for i in range(1 , n + 1):
        l = list(input_list[i].strip().split())

        if l[0] == '1':
            word.append((l[1] , i))

        elif l[0] == '2':
            word.appendleft((l[1] , i))

        else:
            if not word: continue
            if word[-1][1] < word[0][1]:
                word.popleft()

            else:
                word.pop()
    if word:
        return "".join([x[0] for x in word])

    else:
        return "0"
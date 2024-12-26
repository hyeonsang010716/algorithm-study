def solve(Input):
    
    a = int(Input)
    
    if a%5 == 0: answer = (a//5)
    elif a%5 == 1 and a>1: answer = (2+(a//5)-1)
    elif a%5 == 2 and a>7: answer = (4+(a//5)-2)
    elif a%5 == 3: answer = (1+(a//5))
    elif a%5 == 4 and a>4: answer = (3+(a//5)-1)
    else: answer = -1
    return answer
    
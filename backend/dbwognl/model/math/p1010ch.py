def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


    
def solve(input):
    input_list = input.split("\n")
    answer=""
    T=int(input_list[0])
    for i in range(T):
        n,m=map(int,input_list[i+1].split())
        bridge = factorial(m) // (factorial(n) * factorial(m - n))
        answer=answer+str(bridge)+"\n"
    return answer
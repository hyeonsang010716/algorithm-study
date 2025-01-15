import ctypes

example=ctypes.CDLL('./p1010c.so')

def solve(input):
    input_list = input.split("\n")
    answer=""
    T=int(input_list[0])
    for i in range(T):
        N,M=map(int,input_list[i+1].split())
        answer=answer+str(example.getanswer(N,M))+"\n"
    return answer
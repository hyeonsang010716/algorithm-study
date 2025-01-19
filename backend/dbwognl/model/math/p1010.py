from ctypes import CDLL
lib = CDLL(r"C:\Users\dbwog\Desktop\project\backend\dbwognl\model\math\p1010.so")

def solve(input):
    input_list = input.split("\n")
    answer=""
    T=int(input_list[0])
    for i in range(T):
        M,N=map(int,input_list[i+1].split())
        answer=answer+str(lib.getanswer(M,N))+"\n"
    return answer
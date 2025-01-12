
def solve(Input):
    liness= Input
    answer=""
    for lines in liness:
        lines=lines.strip().split('\n')
        T=int(lines[0])
        
    
        for i in range(1,T+1):
            N=int(lines[i])
            a,b=1,0
                
            for j in range(N):
                a,b=b,a+b
            answer+=f"{a} {b}\n"
    print(answer)           
    return answer.strip()

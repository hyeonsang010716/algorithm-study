import math
def solve(Input):
    lines= Input.split('\n')
    T=int(lines[0])
    answer=""
    cases=[]
    for line in lines[1:]:
        case=list(map(int,line.split()))
        cases.append(case)
    for i in range(T):
        x1,y1,r1,x2,y2,r2=cases[i]
        distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
        if(distance>r1+r2 or distance < abs(r1-r2)):
            answer=answer+"0\n"
        elif(r1==r2 and x1==y1 and x2==y2):
            answer=answer+"-1\n"
        elif(distance==r1+r2 or distance==abs(r1-r2)):
            answer=answer+"1\n"
        else:
            answer=answer+"2\n"

    return answer
        
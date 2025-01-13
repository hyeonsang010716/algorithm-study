def solve(Input):
    
    input_list = Input.split("\n")
    
    answers = ""
    
    N = int(input_list[0])
    for i in range(N):
        List = [[1, 0], [0, 1]]
        m = int(input_list[1+i])
        if m == 0 :
            answer = str(List[0][0]) +  " " + str(List[0][1])
        elif m == 1 :
            answer = str(List[1][0]) +  " " + str(List[1][1])
        else:
            x = 2
            while x != m+1 :
                List.append([List[x-2][0] + List[x-1][0] , List[x-2][1] + List[x-1][1]])
                x+= 1
            answer = str(List[x-1][0]) +  " " + str(List[x-1][1])
            
        answers += answer + "\n"
    return answers
    
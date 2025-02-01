def solve(Input):
    
    input_list = Input.split("\n")
    
    answers = ""
    
    N = int(input_list[0])
    for i in range(N):
        S=int(input_list[i+1])
        arr=[0]*11
        arr[1]=1
        arr[2]=2
        arr[3]=4
        for j in range (4,11):
            arr[j]=arr[j-1]+arr[j-2]+arr[j-3]
        for j in range(0,n):
            testNum=int(input_list[i+1])
            answer=answer+str(arr[testNum])+"\n"

    return answers
    
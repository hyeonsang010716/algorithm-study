def solve(input):
    input_list = input.split("\n")
    K=int(input_list[0])
    answers = ""
    stack = []

    for i in range(K) :
        N = int(input_list[i+1])
        if N == 0 :
            stack.pop()
        else :
            stack.append(N)

    return(sum(stack))
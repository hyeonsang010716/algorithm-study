def solve(input):
    results = []
    for input_line in input:
        a, b= input_line.split()
        answer = []
        for i in range(len(b)-len(a)+1):
            count = 0
            for j in range(len(a)):
                if a[j]!=b[i+j]:
                    count+=1
            answer.append(count)
        results.append(str(min(answer)))
    return results

import re

def solve(Input):
    input_list = Input.split("\n")
    
    answers = ""
    
    T = int(input_list[0])
    for i in range(T):
        record = input_list[i+1]
        tmp = re.compile("(100+1+|01)+")
        if tmp.fullmatch(record):
            res = "YES"
        else:
            res = "NO"
        
        answers += res + "\n"
    return answers
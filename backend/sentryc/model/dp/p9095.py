import sys

def solve(Input):
    input_list = Input.split("\n")
    
    answers = ""
    
    t = int(input_list[0])
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(t):
        n = int(input_list[i+1])
        if n > 3:
            for j in range(4, n+1):
                dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        answers += str(dp[n]) + "\n"
    return answers

if __name__=="__main__":
    input_list1 = "3\n4\n7\n10"
    print(solve(input_list1))
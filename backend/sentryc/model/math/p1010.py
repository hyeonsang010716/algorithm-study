def solve(Input):
    input_list = Input.split("\n")
    
    answers = ""
    
    def fac(num):
        ans = 1
        for i in range(1, num+1):
            ans *= i
        return ans

    t = int(input_list[0])
    for i in range(t):
        n, m = map(int, input_list[i+1].split())
        res = fac(m) // (fac(n) * fac(m-n))
        
        answers += str(res) + "\n"
    return answers
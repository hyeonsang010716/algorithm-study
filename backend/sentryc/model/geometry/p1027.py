def solve(Input):
    input_list = Input.split("\r\n")
    
    answers = ""
    
    def cnt_vaild(idx):
        rep = max(idx+1, n - idx)
        cnt, left_grad, right_grad = 0, float('inf'), float('inf')
        for i in range(1, rep):
            left_idx = idx - i
            right_idx = idx + i
            if left_idx >= 0:
                temp_grad = (buliding_li[idx] - buliding_li[left_idx]) / i
                if temp_grad < left_grad:
                    left_grad = temp_grad
                    cnt += 1
            if right_idx < n:
                temp_grad = (buliding_li[idx] - buliding_li[right_idx]) / i
                if temp_grad < right_grad:
                    right_grad = temp_grad
                    cnt += 1

        return cnt

    n = int(input_list[0])
    buliding_li = list(map(int, input_list[1].split()))
    res = 0
    for i in range(n):
        res = max(res, cnt_vaild(i))    
        
    answers += str(res) + "\n"
    
    return answers

if __name__== "__main__":
    input_list1 = "15\n1 5 3 2 6 3 2 6 4 2 5 7 3 1 5"
    input_list2 = "1\n10"
    print(solve(input_list1))
    print(solve(input_list2))
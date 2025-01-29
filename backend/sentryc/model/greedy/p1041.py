def solve(Input):
    input_list = Input.split("\r\n")
    
    answers = ""
    
    def cal_min1(n):
        return min(li) * (n-2) * (n-2) * 5

    def cal_min2(n):
        cp_li = li.copy()
        
        tmp1 = min(li)
        idx = li.index(tmp1)
        cp_li.remove(tmp1)
        cp_li.remove(li[5 - idx])
        tmp2 = min(cp_li)
        
        if tmp1 < tmp2: minus_val = tmp2
        else: minus_val = tmp1
        
        min2 = tmp1 + tmp2
        return (min2 * (n-2) * 12) - (minus_val * (n-2) * 4)

    def cal_min3():
        min3, minus_val = 0, 0
        for i in range(3):
            temp = min(li[i], li[5 - i])
            if temp > minus_val:
                minus_val = temp
            min3 += temp
        return (8 * min3) - (4 * minus_val)

    n = int(input_list[0])
    li = list(map(int, input_list[1].split()))

    res = 0
    if n == 1:
        res = sum(li) - max(li)
    elif n == 2:
        res = cal_min3()
    else:
        res = cal_min1(n) + cal_min2(n) + cal_min3()

    answers += str(res) + "\n"
    return answers

if __name__=="__main__":
    input_list1 = "2\r\n1 2 3 4 5 6"
    print(solve(input_list1))
    input_list2 = "3\r\n1 2 3 4 5 6"
    print(solve(input_list2))
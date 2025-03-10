def solve(n):
    if n % 5 == 0:  # 5로 나눠떨어질 때
        return str(n // 5)
    else:
        p = 0
        while n > 0:
            n -= 3
            p += 1
            if n % 5 == 0:  # 3kg과 5kg를 조합해서 담을 수 있을 때
                p += n // 5
                return str(p)
            elif n == 1 or n == 2:  # 설탕 봉지만으로 나눌 수 없을 때
                return "-1"
            elif n == 0:  # 3으로 나눠떨어질 때
                return str(p)

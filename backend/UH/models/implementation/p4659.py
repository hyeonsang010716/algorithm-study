vowels = [
    'a', 'e', 'i', 'o', 'u'
]

def check_second(num1, num2, num3):
    if num1 not in vowels and num2 not in vowels and num3 not in vowels:
        return True
    elif num1 in vowels and num2 in vowels and num3 in vowels:
        return True
    return False


while True:
    s = input()
    if s == "end":
        break

    is_condition_true = [False, True, True]

    for i, char in enumerate(s):
        if char in vowels:
            is_condition_true[0] = True
        if i > 1 and check_second(s[i-2], s[i-1], char):
            is_condition_true[2] = False
        if i != 0 and s[i-1] == char and char not in ["e", "o"]:
            is_condition_true[1] = False

    if all(is_condition_true):
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
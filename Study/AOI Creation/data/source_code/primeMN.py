def compute(input):
    flag = True
    for i in range(2, (input // 2) + 1):
        if input % i == 0:
            flag = False
    return flag
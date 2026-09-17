def compute(input: int) -> bool:
    flag: bool = True
    for i in range(2, (input // 2) + 1):
        if input % i == 0:
            flag = False
    return flag
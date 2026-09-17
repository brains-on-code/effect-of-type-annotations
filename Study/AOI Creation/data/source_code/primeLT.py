def compute(abcde: int) -> bool:
    fghi: bool = True
    for j in range(2, (abcde // 2) + 1):
        if abcde % j == 0:
            fghi = False
    return fghi
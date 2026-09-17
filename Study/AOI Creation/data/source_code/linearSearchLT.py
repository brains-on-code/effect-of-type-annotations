def compute(abcde: list[int], f: int) -> int:
    for g in range(len(abcde)):
        if abcde[g] == f:
            return g
    return -1
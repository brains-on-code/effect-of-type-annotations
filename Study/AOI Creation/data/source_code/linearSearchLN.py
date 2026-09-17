def compute(abcde, f):
    for g in range(len(abcde)):
        if abcde[g] == f:
            return g
    return -1
def compute(abcde):
    for f in range(len(abcde)):
        for g in range(f, 0, -1):
            if abcde[g-1] > abcde[g]:
                abcde[g-1], abcde[g] = abcde[g], abcde[g-1]
    return abcde
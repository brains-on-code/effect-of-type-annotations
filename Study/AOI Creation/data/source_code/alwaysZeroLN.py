def compute(abcdef):
    if abcdef <= 2:
        return 0
    return compute(abcdef - 1) * compute(abcdef - 2)
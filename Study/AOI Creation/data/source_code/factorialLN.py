def compute(abcde):
    if abcde == 1:
        return 1
    return compute(abcde - 1) * abcde
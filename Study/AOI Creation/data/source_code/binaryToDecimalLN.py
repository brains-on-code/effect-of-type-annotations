def compute(abcdef):
    if abcdef == "0":
        return 0
    if abcdef == "1":
        return 1
    if abcdef[-1] == "0":
        return 2 * compute(abcdef[:-1])
    if abcdef[-1] == "1":
        return 1 + 2 * compute(abcdef[:-1])
    return -1
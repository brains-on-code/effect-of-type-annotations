def compute(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    return a * compute(a, b - 1)
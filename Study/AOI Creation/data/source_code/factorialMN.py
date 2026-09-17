def compute(value):
    if value == 1:
        return 1
    return compute(value - 1) * value
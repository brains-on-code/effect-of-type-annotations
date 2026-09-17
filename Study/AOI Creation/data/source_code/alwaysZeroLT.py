def compute(abcdef: int) -> int:
    if abcdef <= 2:
        return 0
    return compute(abcdef - 1) * compute(abcdef - 2)
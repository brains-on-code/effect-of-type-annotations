def compute(abcdef):
    if abcdef == 0:
        return 0
    return (abcdef % 10) + compute(abcdef // 10)
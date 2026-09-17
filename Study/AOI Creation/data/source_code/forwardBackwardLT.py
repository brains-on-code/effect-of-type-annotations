def compute(abcde: str) -> str:
    f: str = ""
    g: str = ""
    for i in range(len(abcde) - 1, -1, -1):
        f = abcde[i] + f
        g = g + abcde[i]
    return f + g
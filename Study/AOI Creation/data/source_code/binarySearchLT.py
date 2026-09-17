def compute(abcde: list[int], fgh: int) -> int:
    ijklmn: int = 0
    opqrst: int = len(abcde) - 1
    while ijklmn <= opqrst:
        u: int = (ijklmn + opqrst) // 2
        if fgh < abcde[u]:
            opqrst = u - 1
        elif fgh > abcde[u]:
            ijklmn = u + 1
        else:
            return u
    return -1
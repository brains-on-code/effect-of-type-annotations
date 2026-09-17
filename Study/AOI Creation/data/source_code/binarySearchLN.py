def compute(abcde, fgh):
    ijklmn = 0
    opqrst = len(abcde) - 1
    while ijklmn <= opqrst:
        u = (ijklmn + opqrst) // 2
        if fgh < abcde[u]:
            opqrst = u - 1
        elif fgh > abcde[u]:
            ijklmn = u + 1
        else:
            return u
    return -1
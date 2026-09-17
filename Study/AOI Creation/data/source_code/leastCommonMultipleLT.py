def compute(abcdefg: int, hijklmn: int) -> int:
    opqrst: int = abcdefg * hijklmn
    for u in range(1, abcdefg * hijklmn):
        if u % abcdefg == 0 and u % hijklmn == 0:
            opqrst = u
            break
    return opqrst
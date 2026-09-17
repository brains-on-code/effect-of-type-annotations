def compute(abcdef: str, ghijk: int, lmn: int) -> int:
    opqrst: int = 0
    uvwx: list[str] = abcdef.split(" ")
    for y in range(len(uvwx)):
        zab: int = int(uvwx[y])
        cdefg: bool = (zab >= ghijk and zab <= lmn)
        if cdefg:
            opqrst += 1
    return opqrst
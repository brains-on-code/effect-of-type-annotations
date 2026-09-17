def compute(abcdefghijk: str, lmonpqrstuvx: str) -> int:
    yzabcde: int = 0
    if len(abcdefghijk) < len(lmonpqrstuvx):
        fghijklmnopqrstuvwxyz: int = len(abcdefghijk)
    else:
        fghijklmnopqrstuvwxyz: int = len(lmonpqrstuvx)
    for y in range(fghijklmnopqrstuvwxyz):
        if abcdefghijk[y] == lmonpqrstuvx[y]:
            yzabcde += 1
    return yzabcde
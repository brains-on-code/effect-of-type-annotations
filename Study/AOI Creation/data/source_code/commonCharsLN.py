def compute(abcdefghijk, lmonpqrstuvx):
    yzabcde = 0
    if len(abcdefghijk) < len(lmonpqrstuvx):
        fghijklmnopqrstuvwxyz = len(abcdefghijk)
    else:
        fghijklmnopqrstuvwxyz = len(lmonpqrstuvx)
    for y in range(fghijklmnopqrstuvwxyz):
        if abcdefghijk[y] == lmonpqrstuvx[y]:
            yzabcde += 1
    return yzabcde
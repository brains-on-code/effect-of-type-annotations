def compute(abcdef, ghijk, lmn):
    opqrst = 0
    uvwx = abcdef.split(" ")
    for y in range(len(uvwx)):
        zab = int(uvwx[y])
        cdefg = (zab >= ghijk and zab <= lmn)
        if cdefg:
            opqrst += 1
    return opqrst
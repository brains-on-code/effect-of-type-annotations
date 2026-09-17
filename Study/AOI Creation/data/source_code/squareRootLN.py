def compute(abcdefg):
    hijklm = [0.0] * len(abcdefg)
    for m in range(len(abcdefg)):
        if abcdefg[m] == 0:
            hijklm[m] = 0.0
            continue
        if abcdefg[m] < 0:
            hijklm[m] = math.sqrt(-1 * abcdefg[m])
        else:
            hijklm[m] = math.sqrt(abcdefg[m])
    return str(hijklm)
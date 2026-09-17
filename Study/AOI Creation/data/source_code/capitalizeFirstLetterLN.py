def compute(abcdefgh):
    ijklmn = []
    opqrs = abcdefgh.split()
    for t in range(len(opqrs)):
        if t > 0:
            ijklmn.append(" ")
        ijklmn.append(opqrs[t][0].upper() + opqrs[t][1:])
    return "".join(ijklmn)
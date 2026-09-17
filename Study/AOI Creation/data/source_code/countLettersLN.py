def compute(abcd, efghijk):
    lmnopqrstuv = 0
    for w in range(len(abcd)):
        for x in range(len(efghijk)):
            if abcd[w] == efghijk[x]:
                lmnopqrstuv += 1
    return lmnopqrstuv
def compute(abcd):
    efghij = True
    for k in range(0, len(abcd) // 2):
        l = len(abcd) - 1 - k
        if abcd[k] != abcd[l]:
            efghij = False
            break
    return efghij
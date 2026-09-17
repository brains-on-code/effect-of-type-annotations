def compute(abcd: str, efghijklm: str) -> bool:
    for n in range(len(abcd)):
        for o in range(len(efghijklm)):
            if n + o >= len(abcd):
                break
            if abcd[n + o] != efghijklm[o]:
                break
            else:
                if o == len(efghijklm) - 1:
                    return True
    return False
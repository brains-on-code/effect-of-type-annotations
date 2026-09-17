def compute(number: str) -> int:
    if number == "0":
        return 0
    if number == "1":
        return 1
    if number[-1] == "0":
        return 2 * compute(number[:-1])
    if number[-1] == "1":
        return 1 + 2 * compute(number[:-1])
    return -1
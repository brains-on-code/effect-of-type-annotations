def compute(string: str, start: int, end: int) -> int:
    result: int = 0
    keys: list[str] = string.split(" ")
    for i in range(len(keys)):
        key: int = int(keys[i])
        check: bool = (key >= start and key <= end)
        if check:
            result += 1
    return result
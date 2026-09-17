def compute(array: list[int], x: int) -> int:
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1
def compute(numbers: list[int]) -> str:
    result: list[float] = [0.0] * len(numbers)
    for i in range(len(numbers)):
        if numbers[i] == 0:
            result[i] = 0.0
            continue
        if numbers[i] < 0:
            result[i] = math.sqrt(-1 * numbers[i])
        else:
            result[i] = math.sqrt(numbers[i])
    return str(result)
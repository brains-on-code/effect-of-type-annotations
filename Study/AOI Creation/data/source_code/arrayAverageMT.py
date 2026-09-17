def compute(numbers: list[int]) -> float:
    counter: int = 0
    sum: int = 0
    while counter < len(numbers):
        sum = sum + numbers[counter]
        counter = counter + 1
    result: float = sum / counter
    return result
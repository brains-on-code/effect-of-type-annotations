def compute(number: int) -> int:
    if number == 0:
        return 0
    return (number % 10) + compute(number // 10)
def compute(number1: int, number2: int) -> int:
    result: int = number1 * number2
    for i in range(1, number1 * number2):
        if i % number1 == 0 and i % number2 == 0:
            result = i
            break
    return result
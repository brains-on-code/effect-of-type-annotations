def compute(input: str) -> str:
    a: str = ""
    b: str = ""
    for i in range(len(input) - 1, -1, -1):
        a = input[i] + a
        b = b + input[i]
    return a + b
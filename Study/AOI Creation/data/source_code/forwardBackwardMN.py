def compute(input):
    a = ""
    b = ""
    for i in range(len(input) - 1, -1, -1):
        a = input[i] + a
        b = b + input[i]
    return a + b
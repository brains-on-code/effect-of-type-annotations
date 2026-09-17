def compute(string, start, end):
    result = 0
    keys = string.split(" ")
    for i in range(len(keys)):
        key = int(keys[i])
        check = (key >= start and key <= end)
        if check:
            result += 1
    return result
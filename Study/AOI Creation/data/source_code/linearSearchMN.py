def compute(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1
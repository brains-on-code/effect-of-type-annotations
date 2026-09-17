def compute(array, key):
    index1 = 0
    index2 = len(array) - 1
    while index1 <= index2:
        m = (index1 + index2) // 2
        if key < array[m]:
            index2 = m - 1
        elif key > array[m]:
            index1 = m + 1
        else:
            return m
    return -1
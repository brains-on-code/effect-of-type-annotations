def compute(word):
    result = True
    for i in range(0, len(word) // 2):
        j = len(word) - 1 - i
        if word[i] != word[j]:
            result = False
            break
    return result
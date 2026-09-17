def compute(word, substring):
    for i in range(len(word)):
        for j in range(len(substring)):
            if i + j >= len(word):
                break
            if word[i + j] != substring[j]:
                break
            else:
                if j == len(substring) - 1:
                    return True
    return False
def compute(word: str) -> bool:
    result: bool = True
    for i in range(0, len(word) // 2):
        j: int = len(word) - 1 - i
        if word[i] != word[j]:
            result = False
            break
    return result
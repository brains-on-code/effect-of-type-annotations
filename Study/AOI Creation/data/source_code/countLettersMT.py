def compute(word: str, letters: list[str]) -> int:
    letterCount: int = 0
    for i in range(len(word)):
        for j in range(len(letters)):
            if word[i] == letters[j]:
                letterCount += 1
    return letterCount
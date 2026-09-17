def compute(sentence: str) -> str:
    result: list[int] = []
    words: list[str] = sentence.split()
    for i in range(len(words)):
        if i > 0:
            result.append(" ")
        result.append(words[i][0].upper() + words[i][1:])
    return "".join(result)
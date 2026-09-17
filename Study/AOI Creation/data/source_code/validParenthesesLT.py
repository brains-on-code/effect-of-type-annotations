def compute(abcdefgh: str) -> bool:
    ijklm: list[str] = []
    for n in abcdefgh:
        if n == '(':
            ijklm.append(')')
        elif n == '{':
            ijklm.append('}')
        elif n == '[':
            ijklm.append(']')
        elif len(ijklm) == 0 or ijklm.pop() != n:
            return False
    return len(ijklm) == 0
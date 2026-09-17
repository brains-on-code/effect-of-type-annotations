def compute(sentence):
    stack = []
    for i in sentence:
        if i == '(':
            stack.append(')')
        elif i == '{':
            stack.append('}')
        elif i == '[':
            stack.append(']')
        elif len(stack) == 0 or stack.pop() != i:
            return False
    return len(stack) == 0
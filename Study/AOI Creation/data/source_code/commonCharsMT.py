def compute(first_input: str, second_input: str) -> int:
    counter: int = 0
    if len(first_input) < len(second_input):
        length_shortest_input: int = len(first_input)
    else:
        length_shortest_input: int = len(second_input)
    for i in range(length_shortest_input):
        if first_input[i] == second_input[i]:
            counter += 1
    return counter
def compute(numbers):
    counter = 0
    sum = 0
    while counter < len(numbers):
        sum = sum + numbers[counter]
        counter = counter + 1
    result = sum / counter
    return result
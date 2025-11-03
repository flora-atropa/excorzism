def steps(number: int):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    elif isinstance(number, float):
        raise ValueError("Only whole integers!")
    elif number == 1:
        return 0
        
    steps = 0
    next_number = None
    while next_number != 1:
        if number % 2 == 0:
            next_number = number / 2
        else:
            next_number = number * 3 + 1

        steps += 1
        number = next_number

    return steps        

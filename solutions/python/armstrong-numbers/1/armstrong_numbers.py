def is_armstrong_number(number):
    number_as_str = str(number)
    number_length = len(number_as_str)


    sum = 0
    
    for i in number_as_str:
        sum += int(i) ** number_length

    if sum == number:
        return True
    return False
    

def find_floor(instruction: str) -> int:
    """Convert an instruction string to a floor number

    :param instruction: str - the directions Santa is supposed to follow
    :return: int - the floor Santa needs to go to
    """
    
    left_parenthesis_count = instruction.count("(")
    right_parenthesis_count = instruction.count(")")

    floor: int = 0 + left_parenthesis_count - right_parenthesis_count

    return floor

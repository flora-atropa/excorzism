def parse_parenthesis(instruction: str) -> int:
    if instruction == "(":
        return 1
    elif instruction == ")":
        return -1

    raise ValueError("Invalid instruction entered!")


def find_basement_entry(instructions: str) -> int:
    """Find the first instruction to send Santa into the basement

    :param instruction: str - the directions Santa is supposed to follow
    :return: int - the Nth instructions which brings Santa into the basement
    """

    floor = 0
    instruction_count = 0
    
    while 0 <= floor:
        floor += parse_parenthesis(instructions[instruction_count])
        instruction_count += 1

    return instruction_count

def solve(challenge: str) -> int:
    return find_basement_entry(challenge)

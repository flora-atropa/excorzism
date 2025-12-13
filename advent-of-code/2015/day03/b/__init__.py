class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x}:{self.y}"


def convert_direction_to_ints(direction: str) -> tuple[int, int]:
    if direction == "^":
        return 0, 1
    elif direction == ">":
        return 1, 0
    elif direction == "<":
        return -1, 0
    elif direction == "v":
        return 0, -1
    else:
        raise ValueError("Unknow Direction Input")


def calculate_visited_houses(directions: str) -> list:
    position_santa = Position(0, 0)
    position_robosanta = Position(0, 0)

    visited_houses: list[str] = [str(position_santa), str(position_robosanta)]

    odd = False

    for direction in directions:
        move = convert_direction_to_ints(direction)

        if odd:
            position_robosanta.x += move[0]
            position_robosanta.y += move[1]

            visited_houses.append(str(position_robosanta))
        else:
            position_santa.x += move[0]
            position_santa.y += move[1]

            visited_houses.append(str(position_santa))

        odd = not odd

    return visited_houses


def solve(challenge: str) -> int:
    return len(set(calculate_visited_houses(challenge)))

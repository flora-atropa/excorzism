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
    position = {"x": 0, "y": 0}

    visited_houses: list[str] = [f"{position['x']}:{position['y']}"]

    for direction in directions:
        move = convert_direction_to_ints(direction)

        position["x"] += move[0]
        position["y"] += move[1]

        visited_houses.append(f"{position['x']}:{position['y']}")

    return visited_houses


def solve(challenge: str) -> int:
    return len(set(calculate_visited_houses(challenge)))

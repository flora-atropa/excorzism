def get_two_shortest_sides(sides: tuple[int, int, int]) -> tuple[int, int]:
    return sorted(sides)[0:2]

def calculate_gift_volume(sides: tuple[int, int, int]) -> int:
    return sides[0] * sides[1] * sides[2]

def calculate_ribbon_length(sides: tuple[int, int, int]) -> int:
    short_sides = get_two_shortest_sides(sides)

    return short_sides[0] * 2 + short_sides[1] * 2

def calculate_bow_length(sides: tuple[int, int, int]) -> int:
    return calculate_gift_volume(sides) + calculate_ribbon_length(sides)

def calculate_ribbon_needed(measurements: str) -> int:
    return calculate_bow_length([int(i) for i in measurements.split("x")])

def calculate_total_ribbon_needed(measurements: list[str]) -> int:
    return sum([calculate_ribbon_needed(i) for i in measurements])

def solve(challenge: str) -> int:
    return calculate_total_ribbon_needed(challenge.splitlines())

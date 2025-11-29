def calculate_sides(sides: tuple[int, int, int]) -> tuple[int, int, int]:
    return (
        sides[0] * sides[1], 
        sides[1] * sides[2], 
        sides[2] * sides[0]
    )

def get_smallest_side(sides: tuple[int, int, int]) -> int:
    return sorted(sides)[0]

def calculate_paper_needed(measurements: str) -> int:
    sides = calculate_sides(
        [int(i) for i in measurements.split("x")]
    )

    return (sum(sides) * 2) + get_smallest_side(sides)

def calculate_total_paper_needed(measurements: list[str]) -> int:
    return sum(
        [calculate_paper_needed(i) for i in measurements]
    )

def solve(challenge: str) -> int:
    return calculate_total_paper_needed(challenge.splitlines())

def is_valid_triangle(sides):
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]
    side_ab = side_a + side_b
    side_ac = side_a + side_c
    side_bc = side_b + side_c

    if any([i == 0 for i in sides]):
        return False
    elif side_ab < side_c or side_ac < side_b or side_bc < side_a:
        return False

    return True

def has_two_equal_sides(sides):
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True
    return False

def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    elif sides[0] == sides[1] and sides[0] == sides[2]:
        return True
    return False


def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    elif equilateral(sides):
        return True
    elif has_two_equal_sides(sides):
        return True
    return False


def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    elif equilateral(sides) or isosceles(sides):
        return False
    return True
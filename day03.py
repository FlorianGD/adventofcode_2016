"""AoC 2016: day 3"""

from typing import List


def validate_triangle(a: int, b: int, c: int) -> bool:
    """
    A triangle is valid if the sum of any of 2 sides is bigger than the other
    """
    return a + b > c and a + c > b and b + c > a


def load_input(filename: str) -> List[List[int]]:
    """Returns a list of lists of 3 ints per line"""
    with open(filename, 'r') as f:
        return [[int(i) for i in line.split()] for line in f.readlines()]


day3 = load_input('day03_input.txt')
part1 = sum(validate_triangle(*sides) for sides in day3)
print(f'Solution for part 1: {part1}')

# Part 2
# The triangles are inputed vertically
# As len(day3) % 3 == 0


def validate_vertical(lines: List[List[int]]) -> int:
    """
    Count the valid triangles parsed vertically.
    As the length of the input is a multiple of 3, we read the lines 3 by 3
    and parse 3 triangles.
    """
    valids = 0
    iterator = iter(lines)
    for line in iterator:
        # Iterate 3 by 3
        valids += sum(validate_triangle(*i) for i in zip(line,
                                                         next(iterator),
                                                         next(iterator)))
    return valids


print(f'Solution for part 2: {validate_vertical(day3)}')

"""AoC 2016: Day 18"""
from collections import Counter
from itertools import starmap

# Part 1

INPUT = (
    "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^"
    ".^.^.^.^^..^^^^^...^.....^....^."
)


def below_tile_type(left: str, center: str, right: str) -> str:
    """
    left, center and right are tiles in the above row. It is a trap iif
    - Its left and center tiles are traps, but its right tile is not.
    - Its center and right tiles are traps, but its left tile is not.
    - Only its left tile is a trap.
    - Only its right tile is a trap.
    Trap is ^, safe is .
    """
    if left == "^" and center == "^" and right == ".":
        return "^"
    elif left == "." and center == "^" and right == "^":
        return "^"
    elif left == "^" and center == "." and right == ".":
        return "^"
    elif left == "." and center == "." and right == "^":
        return "^"
    else:
        return "."


def row_below(line: str) -> str:
    """Computes the row below the given line."""
    return "".join(starmap(below_tile_type, zip("." + line, line, line[1:] + ".")))


def fill_rows(fisrt_line: str, nrows: int = 40) -> str:
    prev_row = fisrt_line
    rows = fisrt_line + "\n"
    for _ in range(nrows - 1):
        row = row_below(prev_row)
        prev_row = row
        rows += row + "\n"
    return rows


def count_safe(first_line: str, nrows: int = 40) -> int:
    return Counter(fill_rows(first_line, nrows))["."]


print(f"Solution for part 1: {count_safe(INPUT)}")

# Part 2
# We need to compute the number of safe tiles for 400000 rows


def count_safe_by_row(first_line: str, nrow: int = 40) -> int:
    """For a more efficient solution, keep only one row in memory at a time"""
    counter = Counter(first_line)
    prev_row = first_line
    for _ in range(nrow - 1):
        row = row_below(prev_row)
        counter.update(row)
        prev_row = row
    return counter["."]


print(f"Solution for part 2: {count_safe_by_row(INPUT, 400000)}")

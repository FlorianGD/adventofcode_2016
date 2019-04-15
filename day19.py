"""AoC 2016: Day 19"""

from itertools import compress, cycle
from collections import deque
from math import log

# Part 1
INPUT = 3014603


def last_elf(num_elves: int) -> int:
    """Find the latest elf with presents."""
    # First elf to start is 1. Afterwards, it can be 1 if the last elf in the
    # round has taken the presents, or 0 if not (it will take the presents of
    # the first elf, and he should be removed.)
    start_elf = 1
    next_slice = iter(range(1, num_elves + 1))
    while num_elves > 1:
        next_slice = compress(next_slice, cycle([start_elf, 1 - start_elf]))
        num_elves, start_elf = (num_elves + start_elf) // 2, (num_elves + start_elf) % 2
    return next(next_slice)


print(f"Solution for part 1: {last_elf(INPUT)}")

# Part 2


def last_elf_p2(num_elves: int) -> int:
    """Find part 2 for small num_elves."""
    elves = deque(range(1, num_elves + 1))
    while len(elves) > 1:
        middle = len(elves) // 2
        elves.rotate(-middle - 1)
        elves.pop()
        elves.rotate(middle - 1)
    return elves.pop()


def last_elf_p2_exact(num_elves: int) -> int:
    """Exact solution for part 2. See notebook for explanation."""
    n_pow = int(log(num_elves) / log(3))
    if num_elves == 3 ** n_pow:
        return num_elves
    elif num_elves < 2 * 3 ** n_pow:
        return num_elves - 3 ** n_pow
    else:
        return 2 * num_elves - 3 ** (n_pow + 1)


print(f"Solution for part 2: {last_elf_p2_exact(INPUT)}.")

"""AoC 2016: Day 19"""

from itertools import compress, cycle

# Part 1
INPUT = 3014603


def last_elf(num_elves: int) -> int:
    """Find the latest elf with presents."""
    # First elf to start is 1. Afterwards, it can be 1 if the last elf in the
    # round has taken the presents, or 0 if not (it will take the presents of
    # the first elf, and he should be removed.)
    start_elf = 1
    next_slice = range(1, num_elves + 1)
    while num_elves > 1:
        next_slice = compress(next_slice, cycle([start_elf, 1 - start_elf]))
        num_elves, start_elf = (num_elves + start_elf) // 2, (num_elves + start_elf) % 2
    return next(next_slice)


print(f"Solution for part 1: {last_elf(INPUT)}")

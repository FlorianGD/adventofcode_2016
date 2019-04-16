"""AoC 2016: Day 20"""

from typing import List

# Part 1
day20 = []
with open("./day20_input.txt") as f:
    for line in f:
        a, b = line.split("-")
        day20.append(range(int(a), int(b) + 1))

day20.sort(key=lambda r: r.start)


def find_possibles(ranges: List[range]) -> List[int]:
    lowest_still_possible = 0
    possibles = []
    for r in ranges:
        if r.start <= lowest_still_possible:
            lowest_still_possible = max(lowest_still_possible, r.stop)
        else:
            possibles.extend(list(range(lowest_still_possible, r.start)))
            lowest_still_possible = r.stop
    return possibles


possibles = find_possibles(day20)
print(f"Solution for part 1: {possibles[0]}")
print(f"Solution for part 2: {len(possibles)}")

"""AoC 2016: Day 17"""

from collections import deque
from hashlib import md5
from typing import Dict, Tuple

# Part 1

INPUT = "veumntbg"
START = 0
MOVESET = {"U": -1, "D": 1, "L": -1j, "R": 1j}


def compute_hash(val: str) -> str:
    return md5(val.encode()).hexdigest()


def are_open(path: str) -> Dict[str, bool]:
    """
    First four characters of the hash are used; they represent, respectively,
    the doors up, down, left, and right from your current position. Any b, c,
    d, e, or f means that the corresponding door is open.
    """
    h = compute_hash(path)
    return dict(zip("UDLR", [c in "bcdef" for c in h[:4]]))


def move(pos: complex, path: str) -> Tuple[complex, str]:
    """
    Find open paths in current position, and choose the first one.
    Returns the new position and the new path.
    """
    doors = are_open(path)
    for door, opened in doors.items():
        if opened:
            yield (pos + MOVESET[door], path + door)


def is_valid(pos: complex) -> bool:
    return 0 <= pos.real <= 3 and 0 <= pos.imag <= 3


def breadth_first_search(path: str) -> str:
    """Starting at 0, go through the maze until 3 + 3j is found."""
    init_len = len(path)
    goal = 3 + 3j
    queue = deque([(0, path)])
    while True:
        pos, path = queue.pop()
        for new_pos, new_path in move(pos, path):
            if is_valid(new_pos):
                if new_pos == goal:
                    return new_path[init_len:]
                else:
                    queue.appendleft((new_pos, new_path))


assert breadth_first_search("ihgpwlah") == 'DDRRRD'
assert breadth_first_search('kglvqrro') == 'DDUDRLRRUDRD'
assert breadth_first_search('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'

print(f'Solution for part 1: {breadth_first_search(INPUT)}')

"""AoC 2016: Day 21"""

from collections import deque
from typing import Deque, List


def swap_position(x: int, y: int, password: Deque) -> None:
    """Swap position x with position y in place."""
    letter_x, letter_y = password[x], password[y]
    password[x] = letter_y
    password[y] = letter_x


def swap_letter(x: str, y: str, password: Deque) -> None:
    """Swap letter x with letter y in place."""
    pos_x, pos_y = password.index(x), password.index(y)
    password[pos_x] = y
    password[pos_y] = x


def rotate(steps: int, orient: str, password: Deque) -> None:
    """Rotate left/right X steps means that the whole deque should be rotated"""
    sign = 1 if orient == "right" else -1
    password.rotate(sign * steps)


def rotate_letter(letter: str, password: Deque) -> None:
    """
    Rotate based on position of letter X means that the whole string should be
    rotated to the right based on the index of letter X (counting from 0) as
    determined before this instruction does any rotations. Once the index is
    determined, rotate the string to the right one time, plus a number of times
    equal to that index, plus one additional time if the index was at least 4.
    """
    steps = password.index(letter)
    steps = steps + 2 if steps >= 4 else steps + 1
    rotate(steps, "right", password)


def reverse_position(x: int, y: int, password: Deque) -> None:
    """
    Reverse positions X through Y means that the span of letters at indexes X
    through Y (including the letters at X and Y) should be reversed in order.
    """
    mid = (y + 1 - x) // 2
    for i in range(mid):
        swap_position(x + i, y - i, password)


def move(x: int, y: int, password: Deque) -> None:
    """
    move position X to position Y means that the letter which is at
    index X should be removed from the string, then inserted such that
    it ends up at index Y.
    """
    letter = password[x]
    del password[x]
    password.insert(y, letter)


def scramble(text: List[str], password: Deque) -> str:
    for line in text:
        instruction, precision, *rest = line.split(" ")
        if instruction == "swap":
            if precision == "position":
                swap_position(int(rest[0]), int(rest[-1]), password)
            else:
                swap_letter(rest[0], rest[-1], password)
        elif instruction == "rotate":
            if precision == "based":
                rotate_letter(rest[-1], password)
            else:
                rotate(int(rest[0]), precision, password)
        elif instruction == "reverse":
            reverse_position(int(rest[0]), int(rest[-1]), password)
        else:  # move
            move(int(rest[0]), int(rest[-1]), password)

    return "".join(password)


test_text = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d""".splitlines()
assert scramble(test_text, deque("abcde")) == "decab"

with open("./day21_input.txt") as f:
    day21 = f.read().splitlines()

print(f'Solution for part 1: {scramble(day21, deque("abcdefgh"))}')

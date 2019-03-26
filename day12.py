"""AoC 2016: Day 12"""
from typing import List
# Part 1

REGISTERS = [0, 0, 0, 0]
NAMES = {"a": 0, 'b': 1, 'c': 2, 'd': 3}


def cpy(reg: List[int], x: str, y: str) -> int:
    """
    Copy x (either val or register) to y in reg in place.
    Returns 1 (means next instruction).
    """
    target = NAMES[y]
    try:
        x = int(x)
    except ValueError:
        x = reg[NAMES[x]]
    reg[target] = x
    return 1


def inc(reg: List[int], x: str) -> int:
    """
    Increases register x by 1 in place.
    Returns 1 (means next instruction).
    """
    reg[NAMES[x]] += 1
    return 1


def dec(reg: List[int], x: str) -> int:
    """
    Decreases register x by 1 in place.
    Returns 1 (means next instruction).
    """
    reg[NAMES[x]] -= 1
    return 1

# jnz x y jumps to an instruction y away (positive means forward; negative
# means backward), but only if x is not zero.


def jnz(reg: List[int], x: str, y: str) -> int:
    """
     Jumps to an instruction y away (positive means forward; negative means
     backward), but only if x is not zero.
     Returns y or 1.
    """
    try:
        x = int(x)
    except ValueError:
        x = reg[NAMES[x]]
    if x != 0:
        return int(y)
    return 1


def run(reg: List[int], instrunctions: List[List[str]]) -> int:
    """
    Runs the instructions and returns the value of register a after a move
    beyond the last instruction.
    """
    i = 0
    while True:
        try:
            instr, *args = instrunctions[i]
            i += eval(instr)(reg, *args)
        except IndexError:
            return reg[0]


with open('day12_input.txt') as f:
    day12 = [l.split() for l in f.readlines()]

print(f'Solution for part 1: {run(REGISTERS, day12)}')

# Part 2

# REG = [0, 0, 1, 0]
# print(f'Solution for part 2: {run(REG, day12)}')

"""AoC 2016: Day 12"""
from typing import List

# Part 1

REGISTERS = [0, 0, 0, 0]
NAMES = {"a": 0, "b": 1, "c": 2, "d": 3}


def cpy(reg: List[int], x: str, y: str) -> int:
    """
    Copy x (either val or register) to y in reg in place.
    Returns 1 (means next instruction).
    """
    target = NAMES[y]
    try:
        value = int(x)
    except ValueError:
        value = reg[NAMES[x]]
    reg[target] = value
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
        value = int(x)
    except ValueError:
        value = reg[NAMES[x]]
    if value != 0:
        return int(y)
    return 1


def run(reg: List[int], instructions: List[List[str]]) -> int:
    """
    Runs the instructions and returns the value of register a after a move
    beyond the last instruction.
    """
    i = 0
    while True:
        try:
            instr, *args = instructions[i]
            i += eval(instr)(reg, *args)
        except IndexError:
            return reg[0]


with open("day12_input.txt") as f:
    day12 = [l.split() for l in f.readlines()]

if __name__ == "__main__":
    print(f"Solution for part 1: {run(REGISTERS, day12)}")

# Part 2

# REG = [0, 0, 1, 0]
# Breaking down what the algorithm actually does, we speed things up a lot

a = b = c = 1
d = 26

c = 7
d += c  # d = 33

while d != 0:
    c = a  # a = c =1
    a += b  # a= 2, b=0, c=1, d=33
    b = c  # b = c = prev_a
    d -= 1

c = 16
while c != 0:
    d = 17
    a += d
    c -= 1

if __name__ == "__main__":
    print(f"Solution for part 2: {a}")

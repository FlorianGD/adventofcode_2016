"""AoC 2016 day 8"""
from collections import namedtuple
from typing import List

import numpy as np

# Part 1
GRID = np.zeros(shape=(6, 50), dtype=int)
Instr = namedtuple('Instruction', ["operation", "value"])


def parse_input(filename: str) -> List[str]:
    with open(filename, "r") as f:
        data = f.read().splitlines()
    day8 = []
    for line in data:
        op, *rest = line.split()
        if op == "rect":
            day8.append(Instr(op, [int(x) for x in rest[0].split('x')]))
        else:
            axis, start, _, step = rest  # eg. row y=0 by 5 -> row, 0, 5
            day8.append(Instr(axis, [int(start[2:]), int(step)]))
    return day8


def light_screen(inst: Instr, grid: np.ndarray) -> None:
    """Compute one instruction and modify grid in place"""
    op = inst.operation
    if op == "rect":
        height, width = inst.value
        grid[:width, :height] = 1
    elif op == "row":
        row_num, step = inst.value
        row = grid[row_num, :]
        grid[row_num, :] = np.roll(row, step)
    else:
        col_num, step = inst.value
        col = grid[:, col_num]
        grid[:, col_num] = np.roll(col, step)


def light_all(instructions: List[Instr], grid: np.ndarray) -> None:
    """Execute all instructions, modifying in place"""
    for inst in instructions:
        light_screen(inst, grid)


day8 = parse_input('day08_input.txt')
light_all(day8, GRID)
print(f'Solution for part 1: {np.sum(GRID)}')

# Part 2
GRID = GRID.astype("str")
GRID[GRID == "1"] = "#"
GRID[GRID == "0"] = "."
print("\n".join("".join(y for y in x) for x in GRID))
print(f'Solution for part 2: ZFHFSFOGPO')

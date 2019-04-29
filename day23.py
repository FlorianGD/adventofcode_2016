"""AoC 2016: Day 23"""
from day12 import cpy, inc, dec, NAMES, REGISTERS  # noqa
from typing import List

# Part 1

REGISTERS[0] = 7


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
        try:
            return int(y)
        except ValueError:
            return reg[NAMES[y]]
    return 1


def run(reg: List[int], instructions: List[List[str]]) -> int:
    """
    Runs the instructions and returns the value of register a after a move
    beyond the last instruction.
    """

    def tgl(reg: List[int], x: str) -> int:
        nonlocal instructions
        nonlocal i
        one_args_dict = {"inc": "dec"}
        two_args_dict = {"jnz": "cpy"}
        # Get the value or registry value.
        try:
            value = int(x) + i
        except ValueError:
            value = reg[NAMES[x]] + i
        # If a tgl points outside of the program, do nothing.
        try:
            old_instr, *args = instructions[value]
        except IndexError:
            return 1
        # Rules for toggling either one arg instruction or two.
        if len(args) == 1:
            new_instr = one_args_dict.get(old_instr, "inc")
        elif len(args) == 2:
            new_instr = two_args_dict.get(old_instr, "jnz")
        # Change the instruction
        instructions[value] = [new_instr] + args
        return 1

    i = 0
    while True:
        try:
            instr, *args = instructions[i]
            # If tgl produces an invalid instrcuction, skip it
            try:
                i += eval(instr)(reg, *args)
            except TypeError:
                i += 1
        except IndexError:
            return reg[0]


test_txt = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a""".splitlines()

test_instr = [l.split() for l in test_txt]

assert run([0, 0, 0, 0], test_instr) == 3

with open("day23_input.txt") as f:
    day23 = [l.split() for l in f.readlines()]

print(f"Solution for part 1: {run(REGISTERS, day23)}")

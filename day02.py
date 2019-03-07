"""AoC 2016: Day 2"""
from typing import Tuple, List

import numpy as np

# Part 1


def find_number(instr: str, start_pos=(1, 1)) -> Tuple[int, Tuple[int, int]]:
    """
    Given a series of instructions, find a number. Instructions are U, L, D, R
    for up, left, down and right respectively. Starting at 5 on a keypad (or
    the given `start_pos`), and not moving when we would move out of the keypad
    find the number after all the instructions are processed.
    The keypad:
    1 2 3
    4 5 6
    7 8 9
    eg: find_number('ULL') == 1
    find_number('RRDDD', (0, 0)) == 9
    """
    keypad = np.arange(1, 10).reshape(3, 3)
    position = np.array(start_pos)
    directions = {'U': [-1, 0], 'L': [0, -1], 'D': [1, 0], 'R': [0, 1]}
    for direct in instr:
        position += directions[direct]
        position.clip(0, 2, out=position)
    final_position = tuple(position)
    return keypad[final_position], final_position


def find_combination(instructions: List) -> str:
    """Given a list of instructions, find the combination"""
    start_pos = (1, 1)
    combination = []
    for instr in instructions:
        num, start_pos = find_number(instr, start_pos)
        combination.append(str(num))
    return ''.join(combination)


assert find_combination(['ULL', 'RRDDD', 'LURDL', 'UUUUD']) == '1985'

with open('day02_input.txt', 'r') as f:
    day02 = f.read().splitlines()

print(f'Solution for part 1: {find_combination(day02)}')

# Part 2
# Nom the keypad is
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
# And we start at 5


def find_number2(instr: str, start_pos=(2, 0)) -> Tuple[str, Tuple[int, int]]:
    keypad = np.array([['', '', '1', '', ''],
                       ['', '2', '3', '4', ''],
                       ['5', '6', '7', '8', '9'],
                       ['', 'A', 'B', 'C', ''],
                       ['', '', 'D', '', '']])
    position = np.array(start_pos)
    directions = {'U': [-1, 0], 'L': [0, -1], 'D': [1, 0], 'R': [0, 1]}
    reverse = {'U': 'D', 'L': 'R', 'D': 'U', 'R': 'L'}
    for direct in instr:
        position += directions[direct]
        position.clip(0, 4, out=position)
        if keypad[tuple(position)] == '':
            position += directions[reverse[direct]]
    final_position = tuple(position)
    return keypad[final_position], final_position


def find_combination2(instructions: List) -> str:
    """Given a list of instructions, find the combination"""
    start_pos = (2, 0)
    combination = []
    for instr in instructions:
        num, start_pos = find_number2(instr, start_pos)
        combination.append(num)
    return ''.join(combination)


assert find_combination2(['ULL', 'RRDDD', 'LURDL', 'UUUUD']) == '5DB3'

print(f'Solution for part 2: {find_combination2(day02)}')

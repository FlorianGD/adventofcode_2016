"""AoC 2016 day 01"""
from typing import List


def load_instr(file: str) -> List:
    with open(file, 'r') as f:
        instr = f.read()
    return instr.strip('\n').split(', ')


def compute_distance(instructions: List) -> int:
    """
    Given the instructions, find the final Manhattan distance.

    Instructions are left (L) or right (R) followed by a number.
    We turn 90 degrees left or right and then advance a distance given by the
    number. Starting at 0,0 find the distance of the final coordinate.
    """
    position = 0j
    current_direction = 1
    for direction, *dist in instructions:
        dist = int(''.join(dist))
        if direction == 'L':
            current_direction *= 1j
        else:
            current_direction *= -1j
        position += dist * current_direction
    return int(abs(position.real) + abs(position.imag))


instructions = load_instr("day01_input.txt")
print(f'Solution for part 1: {compute_distance(instructions)}')


# Part 2
def first_visited_twice(instructions: List) -> int:
    """Return the distance of the first location visited twice"""
    position = 0j
    current_dir = 1
    visited = {position}
    for direction, *dist in instructions:
        dist = int(''.join(dist))
        if direction == 'L':
            current_dir *= 1j
        else:
            current_dir *= -1j
        new_positions = {position + i*current_dir for i in range(1, dist)}
        position += dist * current_dir
        result = new_positions.intersection(visited)
        if result:
            result = result.pop()
            return int(abs(result.real) + abs(result.imag))
        visited.update(new_positions)


assert first_visited_twice("R8, R4, R4, R8".split(', ')) == 4
print(f'Solution for part 2: {first_visited_twice(instructions)}')

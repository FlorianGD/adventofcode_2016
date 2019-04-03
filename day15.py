"""AoC 2016 Day 15"""
import re
from dataclasses import dataclass
from typing import List

# Part 1


@dataclass
class Disk:
    num: int
    max_positions: int
    init_pos: int

    def pos(self, t: int) -> int:
        return (self.init_pos + t) % self.max_positions


def read_input(filename: str) -> List[Disk]:
    disks = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            num, max_p, _, init = re.findall(r'\d+', line)
            disks.append(Disk(int(num), int(max_p), int(init)))
    return disks


def fall_through(t0: int, disks: List[Disk]) -> bool:
    """Return True if the capsule goes through all the disks in order"""
    return all(disk.pos(t0 + disk.num) == 0 for disk in disks)


def find_start(disks: List[Disk]) -> int:
    """Find the first start that allows the capsule to fall_trough"""
    t0 = 0
    while True:
        if fall_through(t0, disks):
            return t0
        t0 += 1


day15 = read_input('day15_input.txt')
print(f'Solution for part 1: {find_start(day15)}')

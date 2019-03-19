"""AoC 2016: Day 10"""
import re
from collections import defaultdict
from typing import DefaultDict, Dict, List
from functools import reduce
from operator import mul
# Part 1


def init_bots(file: List[str]) -> DefaultDict[str, Dict]:
    """parse the input file to keep only the initial values"""
    bots = defaultdict(dict)
    name = re.compile(r'(?:bot|output) \d+')
    nums = re.compile(r'\d+')
    for line in file:
        if line.startswith('bot'):
            num, low_to, high_to = name.findall(line)
            bots[num].update({'low_to': low_to,
                              'high_to': high_to})
        else:
            value, num = nums.findall(line)
            bot = bots[f'bot {num}']
            bot['chips'] = bot.get('chips', [])
            bot['chips'].append(int(value))
    return bots


def find_compare(bots: List[DefaultDict[str, Dict]],
                 low: int, high: int) -> str:
    """Find name of the bot responsible for comparison between low and high"""
    while True:
        bots_2_chips = [
            (name, bot)
            for (name, bot) in bots.items()
            if len(bot.get('chips', [])) == 2 and name.startswith('bot')
            ]
        for name, b in bots_2_chips:
            low_val, high_val = sorted(b['chips'])
            b['chips'] = []
            bots[b['low_to']]['chips'] = bots[b['low_to']].get('chips', [])
            bots[b['low_to']]['chips'].append(low_val)
            bots[b['high_to']]['chips'] = bots[b['high_to']].get('chips', [])
            bots[b['high_to']]['chips'].append(high_val)
            if (low_val, high_val) == (low, high):
                return name


with open('day10_input.txt') as f:
    day10 = f.read().splitlines()
bots = init_bots(day10)
print(f'Solution for part 1: {find_compare(bots, 17, 61)}')

# Part 2


def finish(bots: List[DefaultDict[str, Dict]]) -> None:
    """Keep on until there is no more chips to compare"""
    def has_2_chips():
        return [
            (name, b)
            for (name, b) in bots.items()
            if len(b.get('chips', [])) == 2 and name.startswith('bot')
            ]
    while has_2_chips():
        for name, b in has_2_chips():
            low_val, high_val = sorted(b['chips'])
            b['chips'] = []
            bots[b['low_to']]['chips'] = bots[b['low_to']].get('chips', [])
            bots[b['low_to']]['chips'].append(low_val)
            bots[b['high_to']]['chips'] = bots[b['high_to']].get('chips', [])
            bots[b['high_to']]['chips'].append(high_val)


finish(bots)

values = (
    val
    for name, bot in bots.items()
    for val in bot.get('chips', [])
    if name in ['output 0', 'output 1', 'output 2']
    )

print(f'Solution for part 2: {reduce(mul, values)}')

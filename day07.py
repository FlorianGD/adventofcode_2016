"""AoC 2016: Day 07"""
import re
from typing import List

# Part 1
# We want to find abba, i.e. any 4 characters where the last 2 are reversed of
# the first 2. This cannot be 4 same characers.
# We also need this abba to not be inside square brackets

ABBA = re.compile(r'([a-z])([a-z])\2\1')
BRACKETS = re.compile(r'\[([a-z]*)\]')


def is_abba(part: str) -> bool:
    return any(a != b for a, b in ABBA.findall(part))


def detect_abba(address: str) -> bool:
    """
    We want an ABBA match, but not inside the brackets.
    """
    inside_brackets = BRACKETS.findall(address)
    outside_brackets = [s.split(']')[-1] for s in address.split('[')]
    if any(is_abba(s) for s in inside_brackets):
        return False
    return any(is_abba(s) for s in outside_brackets)


assert detect_abba("abba[mnop]qrst")  # ok outside
assert not detect_abba('abcd[bddb]xyyx')  # nok because inside brackets
assert not detect_abba('aaaa[qwer]tyui')  # not ok : characters are the same
assert detect_abba('ioxxoj[asdfgh]zxcvbn')  # ok outside


def load_input(filename: str) -> List[str]:
    with open(filename) as f:
        data = f.read().splitlines()
    return data


day07 = load_input('day07_input.txt')
print(f'Solution for part 1: {sum(detect_abba(l) for l in day07)}')

# Part 2
# We mist find aba outside brackets with corresponding bab inside brackets.
# If so, the address is said to support SSL
# We need to find overlapping groups, so I referred to this SO answer
# https://stackoverflow.com/questions/11430863/how-to-find-overlapping-matches
# -with-a-regexp

ABA = re.compile(r'(?=([a-z])([a-z])\1)')


def support_ssl(address: str) -> bool:
    inside_brackets = BRACKETS.findall(address)
    outside_brackets = [s.split(']')[-1] for s in address.split('[')]
    # Find matches and flatten the list
    inside_matches = [
        a
        for s in inside_brackets if ABA.findall(s)
        for a in ABA.findall(s)
    ]
    outside_matches = [
        a
        for s in outside_brackets if ABA.findall(s)
        for a in ABA.findall(s)
    ]
    return any((b, a) in inside_matches for [a, b] in outside_matches)


assert support_ssl('aba[bab]xyz')
assert not support_ssl('xyx[xyx]xyx')
assert support_ssl('aaa[kek]eke')
assert support_ssl("zazbz[bzb]cdb")

print(f'Solution for part 2: {sum(support_ssl(l) for l in day07)}')

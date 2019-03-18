"""AoC 2016: Day 9"""
import itertools as it
from typing import Iterable
import re
# Part 1
# We have to take the input until we find a parenthesis. Next, it will be in
# the form (12x3) meaning we want the next 12 characters 2 times, whatever they
# are (including parenthesis).
# Whitespaces must be stripped.


def decompress(code: Iterable) -> str:
    code = re.sub(r'\s', '', code)
    code = iter(code)
    while True:
        yield from it.takewhile(lambda x: x != "(", code)
        try:
            num = int(''.join(list(it.takewhile(lambda x: x != 'x', code))))
        except ValueError:  # We reached the end
            break
        times = int(''.join(it.takewhile(lambda x: x != ')', code)))
        yield from it.repeat(''.join(it.islice(code, num)), times)


assert ''.join(decompress("ADVENT")) == "ADVENT"
assert ''.join(decompress('A(1x5)BC')) == 'ABBBBBC'
assert ''.join(decompress('(3x3)XYZ')) == 'XYZXYZXYZ'
assert ''.join(decompress('A(2x2)BCD(2x2)EFG')) == 'ABCBCDEFEFG'
assert ''.join(decompress('(6x1)(1x3)A')) == '(1x3)A'
assert ''.join(decompress('X(8x2)   (3x3)ABCY')) == 'X(3x3)ABC(3x3)ABCY'

with open('day09_input.txt') as f:
    day9 = f.read()

decompressed = ''.join(decompress(day9))
print(f'Solution for part 1: {len(decompressed)}')

# Part 2
# When we read next, we need to also decompress what is inside.
day9 = re.sub(r'\s', '', day9)


def decompress_v2(code: str) -> str:
    if "(" not in code:
        return len(code)
    i = code.index('(')
    j = code.index('x')
    k = code.index(')')
    num = int(code[i+1:j])
    times = int(code[j+1:k])
    to_decompress = code[k+1:k+1+num]
    next_code = code[k+1+num:]
    return i + times * decompress_v2(to_decompress) + decompress_v2(next_code)


assert decompress_v2('(3x3)XYZ') == len('XYZXYZXYZ')
assert decompress_v2('X(8x2)(3x3)ABCY') == len('XABCABCABCABCABCABCY')
assert decompress_v2('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
assert decompress_v2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445  # noqa

print(f'Solution for part 2: {decompress_v2(day9)}')

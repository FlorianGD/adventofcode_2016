"""AoC 2016: Day 14"""
from functools import lru_cache
from hashlib import md5
from itertools import islice
from typing import Generator
import re

# Part 1
SALT = 'ahsbgdzn'
TRIPLE = re.compile(r'(.)\1{2}')


@lru_cache(maxsize=None)
def compute_hash(val: str) -> str:
    return md5(val.encode()).hexdigest()


def find_fivele(salt: str, index: int, char: str) -> bool:
    """Look the next 1000 indexes for 5 times char in a hash"""
    for i in range(index + 1, index + 1001):
        if char * 5 in compute_hash(salt + str(i)):
            return True
    return False


def next_index(salt: str) -> Generator:
    """
    Look for index that produce a triple, followed by a fivele whitin the next
    1000 indexes.
    """
    index = 0
    while True:
        h = compute_hash(salt + str(index))
        m = TRIPLE.search(h)
        if m:
            char = m.group(1)
            if find_fivele(salt, index, char):
                yield index
        index += 1


def all_indexes(salt: str) -> int:
    """
    Find the 64th valid index.
    """
    return list(islice(next_index(salt), 64))


# test_hash = all_indexes('abc')
# assert test_hash[-1] == 22728

sol = all_indexes(SALT)
print(f'Solution for part 1: {sol[-1]}')

# Part 2


@lru_cache(maxsize=None)
def compute_stretched_hash(val: str) -> str:
    for _ in range(2017):
        val = compute_hash(val)
    return val


def find_fivele_stretched(salt: str, index: int, char: str) -> bool:
    """Look the next 1000 indexes for 5 times char in a hash"""
    for i in range(index + 1, index + 1001):
        if char * 5 in compute_stretched_hash(salt + str(i)):
            return True
    return False


def next_index_stretched(salt: str) -> Generator:
    """
    Look for index that produce a triple, followed by a fivele whitin the next
    1000 indexes.
    """
    index = 0
    while True:
        h = compute_stretched_hash(salt + str(index))
        m = TRIPLE.search(h)
        if m:
            char = m.group(1)
            if find_fivele_stretched(salt, index, char):
                yield index
        index += 1


def all_indexes_stretched(salt: str) -> int:
    """
    Find the 64th valid index.
    """
    return list(islice(next_index_stretched(salt), 64))


print(f'Solution for part 2: {all_indexes_stretched(SALT)[-1]}')

"""AoC 2016 Day 5"""
from hashlib import md5
from typing import Optional, Tuple

from tqdm import trange

# Part 1
INPUT = "abbhdwsy"

# The goal is to finf the password from the input. We must pad integers at the
# end of the input until the md5 hash starts with five zeros. The 6th value of
# the hash is then the first letter of the password. We must find a 8 letter
# password.


def next_letter(door_id: str, start: Optional[int] = 0) -> Tuple[int, str]:
    """
    The door_id is the start of the sequence we must hash padding integers from
    start if specified.
    """
    while True:
        h = md5((door_id + str(start)).encode()).hexdigest()
        if h.startswith("00000"):
            break
        else:
            start += 1
    return (start, h[5])


def find_password(door_id: str) -> str:
    password = ""
    start = 0
    for _ in trange(8):
        start, letter = next_letter(door_id, start)
        password += letter
        start += 1
    return password


print(f'Solution for part 1: {find_password(INPUT)}')

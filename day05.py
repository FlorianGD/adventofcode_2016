"""AoC 2016 Day 5"""
from hashlib import md5
from typing import Optional, Tuple, List

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
            return (start, h)
        else:
            start += 1


def find_password(door_id: str) -> Tuple[str, List[Tuple[int, str]]]:
    hashes = []
    password = ""
    start = 0
    for i in trange(8):
        start, h = next_letter(door_id, start)
        hashes.append((start, h))
        password += h[5]
        start += 1
    return password, hashes


password, hash_list = find_password(INPUT)
print(f'Solution for part 1: {password}')


def find_password_p2(door_id: str, init_list: List[Tuple[int, str]]) -> str:
    """
    the 6th character is the position of the letter now if valid (i.e between
    0 and 7), and in this case, the letter is the 7th character.
    init_list is already computed hashes that start with 5 zeros, to save time.
    """
    pwd_list = ['-'] * 8

    def change_pwd_if_valid(hash0: str, pwd: List[str] = pwd_list) -> None:
        """Modifiy pwd in place if valid and not already set"""
        try:
            pos = int(hash0[5], 16)
            if pwd[pos] == '-':
                pwd[pos] = hash0[6]
                print(''.join(pwd))
        except IndexError:
            pass

    # First pass using the already calculated hahses
    for i, hash0 in init_list:
        change_pwd_if_valid(hash0)
    start = i + 1
    while '-' in pwd_list:
        start, hash0 = next_letter(door_id, start=start)
        start += 1
        change_pwd_if_valid(hash0)
    return ''.join(pwd_list)


print(f'Solution for part 2: {find_password_p2(INPUT, hash_list)}')

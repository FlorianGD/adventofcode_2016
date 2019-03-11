"""AoC 2016: day 4"""
import re
from collections import Counter, namedtuple
from string import ascii_lowercase
from typing import List

# Part 1
Room = namedtuple('Room', ['name', 'id', 'sum'])
NAME = re.compile(r'(?P<name>[a-z\-]+)-(?P<id>\d+)\[(?P<sum>[a-z]{5})')


def parse_input(fielname: str) -> List[Room]:
    """Load and parse the input as a list of strings"""
    data = []
    with open(fielname) as f:
        for line in f.read().splitlines():
            data.append(Room(**NAME.search(line).groupdict()))
    return data


def valid_checksum(room: Room) -> bool:
    """
    Valid if the sum is the 5 most common characters from the name in order,
    with the ties broken alphabetically, excluding dashes.
    """
    validation = Counter(sorted(room.name.replace('-', ''))).most_common(5)
    # Counter.most_common(5) can return more than 5 values if there are ties
    cheksum = ''.join(i for i, _ in validation)[:5]
    return cheksum == room.sum


assert valid_checksum(Room('aaaaa-bbb-z-y-x', '123', 'abxyz'))
assert valid_checksum(Room('a-b-c-d-e-f-g-h', '987', 'abcde'))
assert valid_checksum(Room('not-a-real-room', '404', 'oarel'))
assert not valid_checksum(Room('totally-real-room', '200', 'decoy'))


def sum_valid_id(rooms: List[Room]) -> int:
    """
    Sum the id of the valid rooms
    """
    return sum(int(r.id) for r in rooms if valid_checksum(r))


assert sum_valid_id([Room('aaaaa-bbb-z-y-x', '123', 'abxyz'),
                     Room('a-b-c-d-e-f-g-h', '987', 'abcde'),
                     Room('not-a-real-room', '404', 'oarel'),
                     Room('totally-real-room', '200', 'decoy')]) == 1514

input_rooms = parse_input('day04_input.txt')
print(f'Solution for part 1: {sum_valid_id(input_rooms)}')

# Part 2


def decrypt_room(room: Room) -> str:
    """
    room is supposed to be a valid room. We decipher the name by rotating the
    letters as much as the id given. The dashes become spaces.
    """
    shift = int(room.id)
    keys = {'-': ' '}
    for i, l in enumerate(ascii_lowercase):
        keys[l] = ascii_lowercase[(i + shift) % 26]
    return ''.join(keys[letter] for letter in room.name)


def find_north_pole(rooms: List[Room]) -> None:
    """
    We need to find the id of the room where North Pole objects are stored.
    """
    for room in rooms:
        if valid_checksum(room):
            decrypted = decrypt_room(room)
            if 'north' in decrypted:
                print(room.id, decrypted, sep=': ')


find_north_pole(input_rooms)

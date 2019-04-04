"""AoC 2016: Day 16"""

# Part 1
INPUT = '11110010111001001'
SWAP = str.maketrans('01', '10')


def dragon_curve(a: str, disk_length: int) -> str:
    """
    Call the data you have at this point "a".
    Make a copy of "a"; call this copy "b".
    Reverse the order of the characters in "b".
    In "b", replace all instances of 0 with 1 and all 1s with 0.
    The resulting data is "a", then a single 0, then "b".
    Repeat these steps until you have enough data to fill the desired disk.
    """
    while len(a) < disk_length:
        b = a[::-1].translate(SWAP)
        a = a + '0' + b
    return a


assert dragon_curve("1", 3) == "100"
assert dragon_curve("0", 3) == "001"
assert dragon_curve('11111', 11) == '11111000000'
assert dragon_curve('111100001010', 25) == '1111000010100101011110000'


def checksum(data: str):
    """
    The checksum for some given data is created by considering each
    non-overlapping pair of characters in the input data. If the two characters
    match (00 or 11), the next checksum character is a 1. If the characters do
    not match (01 or 10), the next checksum character is a 0. This should
    produce a new string which is exactly half as long as the original. If the
    length of the checksum is even, repeat the process until you end up with a
    checksum with an odd length.
    """
    if len(data) % 2 == 1:
        return data
    it = iter(data)
    new_data = ''
    for bit in it:
        if bit == next(it):  # two consecutive characters are the same
            new_data += '1'
        else:
            new_data += '0'
    return checksum(new_data)


assert checksum('110010110100') == '100'


def final_checksum(init: str, length: int):
    data = dragon_curve(init, length)
    return checksum(data[:length])


assert final_checksum('10000', 20) == '01100'

print(f'Solution for part 1: {final_checksum(INPUT, 272)}')

# Part 2
print(f'Solution for part 2: {final_checksum(INPUT, 35651584)}')

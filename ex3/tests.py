import pytest
from part_numbers import get_part_numbers


engine = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

def test_get_part_numbers():
    assert get_part_numbers(engine) == [467, 35, 633, 617, 592, 755, 664, 598]

def test_sum():
    assert sum(get_part_numbers(engine)) == 4361



if __name__ == '__main__':
    print(get_part_numbers(engine))
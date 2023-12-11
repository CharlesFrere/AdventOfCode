import pytest
import numpy as np
from part1 import expand_universe, get_empty_lines, get_galaxies, sum_distances

EXAMPLE = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#....."
]

EXPANDED_EXAMPLE = [
    "....#........",
    ".........#...",
    "#............",
    ".............",
    ".............",
    "........#....",
    ".#...........",
    "............#",
    ".............",
    ".............",
    ".........#...",
    "#....#......."
]

TEST_GALAXY = np.array([list(line.strip()) for line in EXAMPLE])

TEST_EXPANDED_GALAXY = np.array([list(line.strip()) for line in EXPANDED_EXAMPLE])


def test_get_empty_lines():
    assert get_empty_lines(TEST_GALAXY) == ([3, 7], [2, 5, 8])


def test_expand_universe():
    actual = expand_universe(TEST_GALAXY)
    expected = TEST_EXPANDED_GALAXY
    assert np.array_equal(actual, expected)


def test_sum_distances():
    assert sum_distances(get_galaxies(TEST_EXPANDED_GALAXY)) == 374


if __name__ == '__main__':
    print(test_expand_universe())

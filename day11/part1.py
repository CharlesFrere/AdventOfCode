import numpy as np
from itertools import combinations

GALAXY = '#'


def get_empty_lines(universe):
    m, n = universe.shape
    rows = [i for i in range(m) if GALAXY not in universe[i]]
    columns = [j for j in range(n) if GALAXY not in universe[:, j]]
    return rows, columns


def expand_universe(universe):
    m, n = universe.shape
    rows, columns = get_empty_lines(universe)
    new_m, new_n = len(rows) + m, len(columns) + n
    expanded_universe = np.full((new_m, new_n), '.', dtype=str)

    new_i = 0
    for i in range(m):
        if i not in rows:
            line = []
            for j in range(n):
                if j in columns:
                    # Filling columns with empty cells
                    line.extend(['.'] * 2)
                else:
                    line.extend(universe[i, j])
            expanded_universe[new_i] = line
            new_i += 1
        else:
            new_i += 2
    return expanded_universe


def get_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def get_galaxies(universe):
    m, n = universe.shape
    galaxies = []
    for i in range(m):
        for j in range(n):
            if universe[i, j] == GALAXY:
                galaxies.append((i, j))
    return galaxies


def sum_distances(galaxies):
    sum = 0
    print(galaxies)
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            print("Galaxy pairs: ", galaxies[i], galaxies[j])
            distance = get_distance(galaxies[i], galaxies[j])
            print(distance)
            sum += distance
    return sum
    # galaxy_pairs = combinations(galaxies, 2)
    # print("Galaxy pairs: ", [(pos1, pos2) for pos1, pos2 in galaxy_pairs])
    # galaxy_pairs = combinations(galaxies, 2)
    # distances = [get_distance(pos1, pos2) for pos1, pos2 in galaxy_pairs]
    # print("Distances:", distances)
    # return sum(distances)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        universe = np.array([list(line.strip()) for line in file.readlines()])

    expanded_universe = expand_universe(universe)
    galaxies = get_galaxies(expanded_universe)
    print("The sum of all the shortest distances between the galaxies is ", sum_distances(galaxies))

import numpy as np
import re
from scipy.signal import convolve2d

SYMBOLS = set("*$+#")


def get_neighbours(grid):
    return convolve2d(grid, np.ones((3, 3)), mode='same', boundary='fill', fillvalue=0) - grid


def get_data():
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def is_symbol(elem):
    return elem in SYMBOLS


if __name__ == "__main__":
    engine = get_data()
    get_symbols = np.vectorize(is_symbol)

    char_matrix = np.array([list(line) for line in engine])
    symbol_map = get_symbols(char_matrix)
    number_of_neighbours = get_neighbours(symbol_map)
    part_numbers = []

    for i in range(len(engine)):
        line = engine[i]
        matches = re.finditer(r'\d+', line)
        for match in matches:
            start, end = match.start(), match.end()
            if number_of_neighbours[i, start:end].any():
                part_number = int(line[start:end])
                part_numbers.append(part_number)

    print(sum(part_numbers))

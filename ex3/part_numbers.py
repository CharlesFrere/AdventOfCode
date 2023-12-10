import numpy as np
import re
from scipy.signal import convolve2d

SYMBOLS = {'%', '&', '/', '#', '-', '$', '+', '.', '@', '*', '='}

def get_neighbours(grid):
    return convolve2d(grid, np.ones((3, 3)), mode='same', boundary='fill', fillvalue=0) - grid


def get_data():
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def is_symbol(char):
    return char != "." and not char.isalnum()

def get_part_numbers(engine):
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

    return part_numbers

def get_symbols(engine):
    symbols = set()

    for line in engine:
        for char in line:
            if char.isalnum() or char.isspace():
                continue
            symbols.add(char)

    return symbols

if __name__ == "__main__":
    engine = get_data()
    part_numbers = get_part_numbers(engine)
    print(sum(part_numbers))
    # print(get_symbols(engine))

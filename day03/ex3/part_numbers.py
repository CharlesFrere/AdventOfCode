import numpy as np
import re
from scipy.signal import convolve2d


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


def calculate_gear_ratios(engine):
    get_symbols = np.vectorize(is_symbol)

    char_matrix = np.array([list(line) for line in engine])
    symbol_map = get_symbols(char_matrix)
    number_of_neighbours = get_neighbours(symbol_map)
    gear_ratios = set()

    for i in range(len(engine)):
        line = engine[i]
        for match in re.finditer(r'\d+', line):
            start, end = match.start(), match.end()
            if number_of_neighbours[i, start:end].any():
                gear_numbers = [int(match.group(0)) for match in re.finditer(r'\d+', engine[i])]
                if len(gear_numbers) == 2:
                    gear_ratios.add(gear_numbers[0] * gear_numbers[1])

    return gear_ratios


if __name__ == "__main__":
    engine = get_data()
    part_numbers = get_part_numbers(engine)
    gear_ratios = calculate_gear_ratios(engine)
    
    print("The sum of all the part numbers in the engine schematic is:", sum(part_numbers))
    print("The sum of all the gear ratios in the engine schematic is:", sum(gear_ratios))
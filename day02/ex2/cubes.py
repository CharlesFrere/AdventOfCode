import re


def get_data():
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def get_game_id(game):
    return int(re.findall(r'\d+', game)[0])


def is_a_valid_game(game, limits: list):
    blue_games = [int(str.split(elem, " ")[0]) for elem in re.findall(r'\d+ blue', game)]
    green_games = [int(str.split(elem, " ")[0]) for elem in re.findall(r'\d+ green', game)]
    red_games = [int(str.split(elem, " ")[0]) for elem in re.findall(r'\d+ red', game)]
    if any(x > limits[0] for x in red_games) \
        or any(y > limits[1] for y in green_games) \
            or any(z > limits[2] for z in blue_games):
        return False
    return True


if __name__ == "__main__":
    games = get_data()
    limits = [12, 13, 14]
    id_list = []
    for game in games:
        if is_a_valid_game(game, limits):
            game_id = get_game_id(game)
            id_list.append(game_id)
    id_sum = sum(id_list)
    print(id_sum)





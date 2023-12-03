filename = "input.txt"
with open(filename) as file:
    lines = [line.rstrip() for line in file]


class Round:
    def __init__(self, round_str) -> None:
        self.red = 0
        self.green = 0
        self.blue = 0
        for draw in round_str.split(","):
            quantity, color = draw.split()
            if color == "red":
                self.red = int(quantity)
            elif color == "green":
                self.green = int(quantity)
            elif color == "blue":
                self.blue = int(quantity)
            else:
                print("this should never happen")

    def is_valid(self, red, green, blue):
        if self.red > red or self.green > green or self.blue > blue:
            return False
        return True


def valid(game):
    game = game.split(":")[1]
    rounds = game.split(";")
    for round_str in rounds:
        game_round = Round(round_str)
        if not game_round.is_valid(12, 13, 14):
            return False
    return True


def fewest_quantities(game):
    min_red = 0
    min_green = 0
    min_blue = 0

    game = game.split(":")[1]
    rounds = game.split(";")
    for round_str in rounds:
        game_round = Round(round_str)

        if game_round.red > min_red:
            min_red = game_round.red

        if game_round.green > min_green:
            min_green = game_round.green

        if game_round.blue > min_blue:
            min_blue = game_round.blue
    return min_red, min_green, min_blue


def part_one():
    total = 0
    for game_number, game in enumerate(lines):
        if valid(game):
            total += game_number+1

    print("part1 total:", total)


def part_two():
    total = 0
    for game in lines:
        r, g, b = fewest_quantities(game)
        total += r * g * b
    print("part2 total:", total)


part_one()
part_two()

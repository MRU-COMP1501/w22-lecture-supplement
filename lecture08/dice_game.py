from random import randint
# Read the names of player 1 and player 2
# Roll two dice for each player and add them together
# Print the rolls for each player

def roll_dice():
    # from https://docs.python.org/3/library/random.html
    dice_roll = randint(1, 6) + randint(1, 6)
    magic_formula()
    return dice_roll

def magic_formula():
    pass

def print_results(name, roll):
    print(f'{name} rolled a {roll}!')

def take_turn(player_num):
    name = input(f'Enter the name of player {player_num}: ')
    roll = roll_dice()
    print_results(name, roll)

def main():
    take_turn(1)
    take_turn(2)

main()
# Functions for dice rolls.

import random


def roll(num_dice, sides):

    # Roll any number of dice with any number of sides and adds the results.
    # Example: roll(3, 6) to roll 3d6.
    # Returns the result as an integer.

    result = 0
    for _ in range(num_dice):
        result = result + random.randrange(1, sides+1)
    return result


def rolling(num_dice, sides):

    # Same as roll(), with additional flavour text.
    # Example: rolling(3, 6)
    # 'Rolling 3d6... 13' and returns the result

    result = roll(num_dice, sides)
    print('Rolling', str(num_dice) + 'd' + str(sides) + '...', result)
    return result


def roll_d6(num_dice):

    # Rolls num_dice six sided dice and returns the result.

    result = 0
    for _ in range(num_dice):
        result = result + random.randint(1, 6)
    return result


def main():
    
    # Some examples on how to use the functions.
    
    print(roll(5,6))
    rolling(5,6)
    rolling(2, 20)
    print('You rolled:', roll_d6(1))


if __name__ == '__main__':
    main()

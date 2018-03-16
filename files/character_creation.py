# Author: Graziantonio de Robertis
# Project name: CyberPy2020
# Project description: A Python conversion of the Cyberpunk2020 tabletop RPG.

# This file includes the character creation. Supports both random generation a custom character.

import dice  # module containing dice roll functions.
import character_creation_variables as ccv  # contains lists and dictionaries for customization options.


# Functions setup

def player_selection(options_list, character_dict, dict_key, title=''):
    """
    args:
        title: title to print before listing the options
        options_list: list from character_creation_variables.py containg the various options
        character_dict: dictionary containing the key i need
        dict_key: key for character_dict corresponding to the value i want to set.
    """
    print(title)
    for each_option in range(len(options_list)):
        print(str(each_option + 1) + '.', options_list[each_option])
    while True:
        p_selection = int(input('Your Choice [insert number]: '))
        if 1 <= p_selection <= len(options_list):
            character_dict[dict_key] = options_list[p_selection - 1]
            break
        else:
            print('You must enter a number between 1 and {}.'.format(len(options_list)))
    print('\n')


# General setup

randomized = False  # flag to check if the player chooses a randomized character creation or not

while True:
    choice = input("Insert 'R' for a random character or 'C' for a custom one: ")
    if choice == 'R' or choice == 'r' or choice == 'random':
        randomized = True
        break
    elif choice == 'C' or choice == 'c' or choice == 'custom':
        randomized = False
        break
    else:
        print("Please enter 'R' or 'C'")

print('\n')

# Name, Gender and Age setup.

ccv.lifepath['name'] = input('Name your character: ').title()

while True:
    gender_selection = input('Is {} Male or Female? '.format(ccv.lifepath['name'])).title()
    gender_selection.upper()
    if gender_selection == 'M' or gender_selection == 'MALE' or gender_selection == 'F' or gender_selection == 'FEMALE':
        ccv.lifepath['gender'] = gender_selection
        break
    else:
        print('Please enter [M]ale or [F]emale.')

while True:
    age_selection = int(input('How old is {}? '.format(ccv.lifepath['name'])))
    if age_selection > 16:
        ccv.lifepath['age'] = age_selection
        break
    else:
        print('Your character must be older than 16.')

print('\n')

# Appearance setup.

if randomized:

    selection = dice.roll(1, 10)
    ccv.lifepath['clothes'] = ccv.clothes[selection - 1]
    selection = dice.roll(1, 10)
    ccv.lifepath['hairstyle'] = ccv.hairstyle[selection - 1]
    selection = dice.roll(1, 10)
    ccv.lifepath['accessories'] = ccv.accessories[selection - 1]

else:

    player_selection(ccv.clothes, ccv.lifepath, 'clothes', '### CLOTHING ###')
    player_selection(ccv.hairstyle, ccv.lifepath, 'hairstyle', '### HAIRSTYLE ###')
    player_selection(ccv.accessories, ccv.lifepath, 'accessories', '### ACCESSORIES ###')


def main():

    print('\n')
    print('Wanted: {}'.format(ccv.lifepath['name']))
    print('Sex: {}'.format(ccv.lifepath['gender']))
    print('Age: about {}'.format(ccv.lifepath['age']))
    print('General description:')
    print('Wears {} and {}.'.format(ccv.lifepath['clothes'], ccv.lifepath['accessories']))
    print('Has {} hair.'.format(ccv.lifepath['hairstyle']))


if __name__ == '__main__':
    main()

# Author: Graziantonio de Robertis
# Project name: CyberPy2020
# Project description: A Python conversion of the Cyberpunk2020 tabletop RPG.

# This file includes the character creation. Supports both random generation a custom character.

import dice  # module containing dice roll functions.
import character_creation_variables as ccv  # contains lists and dictionaries for customization options.
import character_class

# Functions setup

def player_selection(options_list, character_object, attr_to_change, title=''):
    """
    args:
        options_list: list from character_creation_variables.py containing the various options
        character_object: Character() object
        attr_to_change: name of the attribute to change, in quotes
        title: title to print before listing the options
    """
    print(title)
    for each_option in range(len(options_list)):
        print(str(each_option + 1) + '.', options_list[each_option])
    while True:
        p_selection = int(input('Your Choice [insert number]: '))
        if 1 <= p_selection <= len(options_list):
            setattr(character_object, attr_to_change, options_list[p_selection - 1])
            break
        else:
            print(f'You must enter a number between 1 and {len(options_list)}')
    print('\n')


def random_selection(options_list, character_object, attr_to_change):
    r_selection = dice.roll(1, len(options_list))
    setattr(character_object, attr_to_change, options_list[r_selection - 1])


# General setup
mc = character_class.Character()  # mc = main character
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

mc.name = input('Name your character: ').title()

while True:
    gender_selection = input(f"Is {mc.name} Male or Female? ").title()
    gender_selection.upper()
    if gender_selection == 'M' or gender_selection == 'MALE' or gender_selection == 'F' or gender_selection == 'FEMALE':
        mc.gender = gender_selection
        break
    else:
        print('Please enter [M]ale or [F]emale.')

while True:
    age_selection = int(input(f"How old is {mc.name}? "))
    if age_selection > 16:
        mc.age = age_selection
        break
    else:
        print('Your character must be older than 16.')

print('\n')

# Appearance setup.

if randomized:

    random_selection(ccv.clothes, mc, 'clothes')
    random_selection(ccv.hairstyle, mc, 'hairstyle')
    random_selection(ccv.accessories, mc, 'accessories')

else:

    player_selection(ccv.clothes, mc, 'clothes', '### CLOTHING ###')
    player_selection(ccv.hairstyle, mc, 'hairstyle', '### HAIRSTYLE ###')
    player_selection(ccv.accessories, mc, 'accessories', '### ACCESSORIES ###')
    print('\n')

# Family background setup.

if randomized:

    # family ranking
    random_selection(ccv.family_ranking, mc, 'family_ranking')

    # parents
    random_selection(ccv.parents, mc, 'parents')

    # if something happened to parents, set what happened
    if mc.parents == 'something happened':
        random_selection(ccv.something_happened, mc, 'something_happened')
    else:
        # mc.parents is already 'both living'
        mc.something_happened = 'N/A'

    # current family status
    random_selection(ccv.family_status, mc, 'family_status')

    # if family in danger, set what's happening
    if mc.family_status == 'in danger':
        random_selection(ccv.family_tragedy, mc, 'family_tragedy')
    else:
        # mcfamily_status is already 'ok, despite everything'
        mc.family_tragedy = 'N/A'

    # childhood
    random_selection(ccv.childhood, mc, 'childhood')

    # siblings
    random_selection(ccv.siblings, mc, 'siblings')

else:

    # family ranking
    player_selection(ccv.family_ranking, mc, 'family_ranking', '### FAMILY RANKING ###')

    # parents
    player_selection(ccv.parents, mc, 'parents', '### PARENTS ###')

    # if something happened to parents, set what happened
    if mc.parents == 'something happened':
        player_selection(ccv.something_happened, mc, 'something_happened', '### SOMETHING HAPPENED ###')
    else:
        # mc.parents is already 'both living'
        mc.something_happened = 'N/A'

    # current family status
    player_selection(ccv.family_status, mc, 'family_status', '### CURRENT FAMILY STATUS ###')

    # if family in danger, set what's happening
    if mc.family_status == 'in danger':
        player_selection(ccv.family_tragedy, mc, 'family_tragedy', "### WHAT'S HAPPENING ###")
    else:
        # mc.family_status is already 'ok, despite everything'
        mc.family_tragedy = 'N/A'

    # childhood
    player_selection(ccv.childhood, mc, 'childhood', '### CHILDHOOD ENVIRONMENT ###')

    # siblings
    player_selection(ccv.siblings, mc, 'siblings', '### SIBLINGS ###')

# personal motivations

if randomized:

    # personality traits
    random_selection(ccv.personality_traits, mc, 'personality_traits')

    # most_valuable_person
    random_selection(ccv.most_valuable_person, mc, 'most_valuable_person')

    # most_valuable_thing
    random_selection(ccv.most_valuable_thing, mc, 'most_valuable_thing')

    # feelings_about_people
    random_selection(ccv.feelings_about_people, mc, 'feelings_about_people')

    # most_valuable_possession
    random_selection(ccv.most_valuable_possession, mc, 'most_valuable_possession')


def main():

    print('\n')
    print(f"Wanted: {mc.name}")
    print(f"Sex: {mc.gender}")
    print(f"Age: about {mc.age}")
    print('\n')
    print('General description:')
    print(f"Wears {mc.clothes} and {mc.accessories}.")
    print(f"Has {mc.hairstyle} hair.")


if __name__ == '__main__':
    main()

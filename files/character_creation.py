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
        options_list: list from character_creation_variables.py containing the various options
        character_dict: dictionary containing the key i need, found in character_creation_variables.py
        dict_key: key for character_dict corresponding to the value i want to set.
        title: title to print before listing the options
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
            print(f'You must enter a number between 1 and {len(options_list)}')
    print('\n')


def random_selection(options_list, character_dict, dict_key):
    r_selection = dice.roll(1, len(options_list))
    character_dict[dict_key] = options_list[r_selection - 1]


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
    gender_selection = input(f"Is {ccv.lifepath['name']} Male or Female? ").title()
    gender_selection.upper()
    if gender_selection == 'M' or gender_selection == 'MALE' or gender_selection == 'F' or gender_selection == 'FEMALE':
        ccv.lifepath['gender'] = gender_selection
        break
    else:
        print('Please enter [M]ale or [F]emale.')

while True:
    age_selection = int(input(f"How old is {ccv.lifepath['name']}? "))
    if age_selection > 16:
        ccv.lifepath['age'] = age_selection
        break
    else:
        print('Your character must be older than 16.')

print('\n')

# Appearance setup.

if randomized:

    random_selection(ccv.clothes, ccv.lifepath, 'clothes')
    random_selection(ccv.hairstyle, ccv.lifepath, 'hairstyle')
    random_selection(ccv.accessories, ccv.lifepath, 'accessories')

else:

    player_selection(ccv.clothes, ccv.lifepath, 'clothes', '### CLOTHING ###')
    player_selection(ccv.hairstyle, ccv.lifepath, 'hairstyle', '### HAIRSTYLE ###')
    player_selection(ccv.accessories, ccv.lifepath, 'accessories', '### ACCESSORIES ###')
    print('\n')

# Family background setup.

if randomized:

    # family ranking
    random_selection(ccv.family_ranking, ccv.lifepath, 'family_ranking')

    # parents
    random_selection(ccv.parents, ccv.lifepath, 'parents')

    # if something happened to parents, set what happened
    if ccv.lifepath['parents'] == 'something happened':
        random_selection(ccv.something_happened, ccv.lifepath, 'something_happened')
    else:
        # ccv.lifepath['parents'] is already 'both living'
        ccv.lifepath['something_happened'] = 'N/A'

    # current family status
    random_selection(ccv.family_status, ccv.lifepath, 'family_status')

    # if family in danger, set what's happening
    if ccv.lifepath['family_status'] == 'in danger':
        random_selection(ccv.family_tragedy, ccv.lifepath, 'family_tragedy')
    else:
        # ccv.lifepath['family_status'] is already 'ok, despite everything'
        ccv.lifepath['family_tragedy'] = 'N/A'

    # childhood
    random_selection(ccv.childhood, ccv.lifepath, 'childhood')

    # siblings
    random_selection(ccv.siblings, ccv.lifepath, 'siblings')

else:

    # family ranking
    player_selection(ccv.family_ranking, ccv.lifepath, 'family_ranking', '### FAMILY RANKING ###')

    # parents
    player_selection(ccv.parents, ccv.lifepath, 'parents', '### PARENTS ###')

    # if something happened to parents, set what happened
    if ccv.lifepath['parents'] == 'something happened':
        player_selection(ccv.something_happened, ccv.lifepath, 'something_happened', '### SOMETHING HAPPENED ###')
    else:
        # ccv.lifepath['parents'] is already 'both living'
        ccv.lifepath['something_happened'] = 'N/A'

    # current family status
    player_selection(ccv.family_status, ccv.lifepath, 'family_status', '### CURRENT FAMILY STATUS ###')

    # if family in danger, set what's happening
    if ccv.lifepath['family_status'] == 'in danger':
        player_selection(ccv.family_tragedy, ccv.lifepath, 'family_tragedy', "### WHAT'S HAPPENING ###")
    else:
        # ccv.lifepath['family_status'] is already 'ok, despite everything'
        ccv.lifepath['family_tragedy'] = 'N/A'

    # childhood
    player_selection(ccv.childhood, ccv.lifepath, 'childhood', '### CHILDHOOD ENVIRONMENT ###')

    # siblings
    player_selection(ccv.siblings, ccv.lifepath, 'siblings', '### SIBLINGS ###')

# personal motivations

if randomized:

    # personality traits
    random_selection(ccv.personality_traits, ccv.lifepath, 'personality_traits')

    # most_valuable_person
    random_selection(ccv.most_valuable_person, ccv.lifepath, 'most_valuable_person')

    # most_valuable_thing
    random_selection(ccv.most_valuable_thing, ccv.lifepath, 'most_valuable_thing')

    # feelings_about_people
    random_selection(ccv.feelings_about_people, ccv.lifepath, 'feelings_about_people')

    # most_valuable_possession
    random_selection(ccv.most_valuable_possession, ccv.lifepath, 'most_valuable_possession')


def main():

    # print('\n')
    # print(f"Wanted: {ccv.lifepath['name']}")
    # print(f"Sex: {ccv.lifepath['gender']}")
    # print(f"Age: about {ccv.lifepath['age']}")
    # print('\n')
    # print('General description:')
    # print(f"Wears {ccv.lifepath['clothes']} and {ccv.lifepath['accessories']}.")
    # print(f"Has {ccv.lifepath['hairstyle']} hair.")

    # TEST (check if everything is stored correctly)
    print('\n')
    print(ccv.lifepath)


if __name__ == '__main__':
    main()

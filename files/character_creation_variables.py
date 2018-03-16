# This module contains all the variables used in character_creation.py

# dictionary containing all the fields about appearance and clothing

lifepath = {'name': '',
            'gender': '',
            'age': '',

            'clothes': '',
            'hairstyle': '',
            'accessories': '',

            'family_ranking': '',
            'parents': '',
            'something_happened': '',
            'family_status': '',
            'childhood': '',
            'family_tragedy': '',
            'siblings': ''
            }

# appearance lists. Elements on these lists will appear in the character customization if the player decides to create
# a custom character.

clothes = ['biker leathers', 'blue jeans', 'corporate suit', 'jumpsuit', 'miniskirt',
           'high fashion clothes', 'camo clothing', 'everyday clothes', 'revealing clothes', 'bag lady chic clothes']

hairstyle = ['mohawk', 'long and ratty', 'short and spiked', 'wild', 'bald', 'striped',
             'tinted', 'neat and short', 'short and curly', 'long and straight']

accessories = ['tatoos', 'mirror shades', 'ritual scars', 'spiked gloves', 'nose rings',
               'fancy earrings', 'long fingernails', 'spike heeled boots', 'weird contact lenses', 'fingerless gloves']

# family background lists.

family_ranking = ['corporate executive', 'corporate manager', 'corporate technician', 'nomad pack', 'pirate fleet',
                  'gang family', 'crime lords', 'combat zone poor people', 'urban homeless', 'arcology family']

parents = ['both living', 'something happened']

something_happened = ['KIA', 'died in an accident', 'were murdered', "have amnesia and don't remember you",
                      'unknown to you', 'hiding', 'have left you to some relatives', 'unregistered',
                      'gave you up for adoption', 'sold you for money']

family_status = ['in danger', 'ok, despite everything']

childhood = ['on the Street, unsupervised', 'in a safe corporate suburbia', 'in a nomad pack',
             'in a decayed neighborhood', 'in a defended corporate zone of the central City', 'in the Combat Zone',
             'in a small village far from the city', 'in a large arcology', 'in a pirate pack',
             'in a research facility']

family_tragedy = ['lost everything through betrayal.', 'lost everything through bad management.', 'got exiled.',
                  'is imprisoned and you alone escaped.', 'vanished. And you are the only remaining member.',
                  'was murdered and you are the only survivor.', 'is involved in a crime organization.',
                  'was scattered to the winds due to misfortune.', 'is cursed with a hereditary feud.',
                  'had a huge debt. Now you have to repay it.']

siblings = ['dislikes you.', 'likes you.', "doesn't care about you", 'worships you as a hero.', 'hates you.']


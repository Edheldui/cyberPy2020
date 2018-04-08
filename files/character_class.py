class Character:

    def __init__(self):
        # general
        self.name = None
        self.gender = None
        self.age = 0

        # look
        self.clothes = None
        self.hairstyle = None
        self.accessories = None

        # family background
        self.family_ranking = None
        self.parents = None
        self.something_happened = None
        self.family_status = None
        self.childhood = None
        self.family_tragedy = None
        self.siblings = None

        # personal motivation
        self.personality_traits = None
        self.most_valuable_person = None
        self.most_valuable_thing = None
        self.feelings_about_people = None
        self.most_valuable_possession = None

    def set_general(self, name, gender, age):
        self.name = name.title()
        self.gender = gender
        self.age = age

    def set_look(self, clothes, hairstyle, accessories):
        self.clothes = clothes
        self.hairstyle = hairstyle
        self.accessories = accessories

    def set_family_background(self, family_ranking, parents, something_happened, family_status, childhood,
                              family_tragedy, siblings):
        self.family_ranking = family_ranking
        self.parents = parents
        self.something_happened = something_happened
        self.family_status = family_status
        self.childhood = childhood
        self.family_tragedy = family_tragedy
        self.siblings = siblings

    def set_personal_motivation(self, personality_traits, most_valuable_person, most_valuable_thing,
                                feelings_about_people, most_valuable_possession):
        self.personality_traits = personality_traits
        self.most_valuable_person = most_valuable_person
        self.most_valuable_thing = most_valuable_thing
        self.feelings_about_people = feelings_about_people
        self.most_valuable_possession = most_valuable_possession


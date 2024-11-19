import random

FACTORY_NEW_BOUND = 0.07
MINIMAL_WEAR_BOUND = 0.15
FIELD_TESTED_BOUND = 0.38
WELL_WORN_BOUND = 0.45
BATTLE_SCARRED_BOUND = 1.00

class Item:
    def __init__(self, id, name, weapon, category, pattern, min_float, max_float, rarity, paint_index, wear, collections):
        self.id = id
        self.name = name
        self.weapon = weapon
        self.category = category
        self.pattern = pattern
        self.min_float = min_float
        self.max_float = max_float
        self.rarity = rarity
        self.paint_index = paint_index
        self.wear = wear
        self.collections = collections
        self.price = random.uniform(0, 500)
        self.float = self.calculate_float()
        self.upperSkins = []
    def __repr__(self):
        return f"Item({self.name}, {self.weapon['name']}, {self.rarity['name']}, {self.category['name']}, {self.wear['name']}, {self.price})"

    def calculate_float(self):
        quality = self.wear['name']
        lower_bound = self.min_float
        upper_bound = self.max_float
        if quality == 'Factory New':
            upper_bound = FACTORY_NEW_BOUND if FACTORY_NEW_BOUND < upper_bound else upper_bound

        if quality == 'Minimal Wear':
            lower_bound = FACTORY_NEW_BOUND if FACTORY_NEW_BOUND > lower_bound else lower_bound
            upper_bound = MINIMAL_WEAR_BOUND if MINIMAL_WEAR_BOUND < upper_bound else upper_bound

        if quality == 'Field-Tested':
            lower_bound = MINIMAL_WEAR_BOUND if MINIMAL_WEAR_BOUND > lower_bound else lower_bound
            upper_bound = FIELD_TESTED_BOUND if FIELD_TESTED_BOUND < upper_bound else upper_bound

        if quality == 'Well-Worn':
            lower_bound = FIELD_TESTED_BOUND if FIELD_TESTED_BOUND > lower_bound else lower_bound
            upper_bound = WELL_WORN_BOUND if WELL_WORN_BOUND < upper_bound else upper_bound

        if quality == 'Battle-Scarred':
            lower_bound = WELL_WORN_BOUND if WELL_WORN_BOUND > lower_bound else lower_bound


        return (lower_bound + upper_bound) / 2



class Collection:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.skins = {}
        self.skins['Consumer Grade'] = []
        self.skins['Industrial Grade'] = []
        self.skins['Mil-Spec Grade'] = []
        self.skins['Restricted'] = []
        self.skins['Classified'] = []
        self.skins['Covert'] = []


    def __repr__(self):
        return f"{self.name}: {self.skins}"
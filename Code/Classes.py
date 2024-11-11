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
        self.price = 0

    def __repr__(self):
        return f"Item({self.name}, {self.weapon['name']}, {self.rarity['name']}, {self.category['name']}, {self.wear['name']}, {self.price})"


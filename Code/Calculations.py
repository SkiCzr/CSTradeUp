
import pickle
from Classes import Item
import itertools

FACTORY_NEW_BOUND = 0.07
MINIMAL_WEAR_BOUND = 0.15
FIELD_TESTED_BOUND = 0.38
WELL_WORN_BOUND = 0.45
BATTLE_SCARRED_BOUND = 1.00

with open("skins_by_rarity.pkl", "rb") as f:
    skins_by_rarity = pickle.load(f)

with open("skins.pkl", "rb") as f:
    skins = pickle.load(f)
z = 0

def classify_quality(avg_float):
    if avg_float < FACTORY_NEW_BOUND:
        return "Factory New"
    if avg_float < MINIMAL_WEAR_BOUND:
        return "Minimal Wear"
    if avg_float < FIELD_TESTED_BOUND:
        return "Field-Tested"
    if avg_float < WELL_WORN_BOUND:
        return "Well-Worn"
    if avg_float < BATTLE_SCARRED_BOUND:
        return "Battle-Scarred"


combinations = itertools.combinations_with_replacement(skins_by_rarity['Consumer Grade'], 10)

for combination in combinations:
    for i in combination:
        i.price = 1
    print(z)
    z += 1
    avg_float = sum(itm.float for itm in combination) / 10
    quality = classify_quality(avg_float)
    price = 0
    revenue = 0
    outcomes = []
    for item in combination:
        price += item.price
        outcomes.extend(list(filter(lambda itm: itm.wear['name'] == quality, item.upperSkins)))
    prob = 1/len(outcomes)
    for out in outcomes:
        revenue += prob * out.price
    profit = revenue - price
    if profit > 0:
        for item in combination:
            print(item.price," ")
        print("\n")
        for item in outcomes:
            print(item.price," ")
        print("Pure profit:",profit,"$"," Multiplier:x", revenue/price)
    break

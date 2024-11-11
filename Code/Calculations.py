
import pickle
from Classes import Item

with open("items.pkl", "rb") as f:
    items = pickle.load(f)

z = 0
for item in items:
    if item.price != 0 :
        z += 1
        print(item)
print(z)
print(len(items))
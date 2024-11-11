import json
import pickle
import random
import time
import urllib

import requests

from Code.Classes import Item


def wait_random_time():
    delay = random.uniform(2, 4)  # Generates a float between 2 and 4
    print(f"Waiting for {delay:.2f} seconds...")
    time.sleep(delay)
    print("Done waiting!")

def get_median_price(item, cont):
    base_url = "https://steamcommunity.com/market/priceoverview/"
    app_id = 730  # App ID for CS2
    currency = 3  # Currency code for Euros, can change if needed

    # Format the market hash name as "Desert Eagle | Ocean Drive (Factory New)"
    market_hash_name = f"{item.name} ({item.wear['name']})"
    encoded_name = urllib.parse.quote(market_hash_name)

    # Construct the request URL
    url = f"{base_url}?appid={app_id}&currency={currency}&market_hash_name={encoded_name}"
    print(url)
    try:
        # Make the request
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Check for a successful response and retrieve median price
        if data.get("success"):
            price_str= data.get("lowest_price")
            if price_str != None:
                price_str = price_str.replace("€", "").replace(",", ".").replace("--", "00").replace(" ", "").strip()
                item.price = float(price_str)
                print(f"The lowest price of '{market_hash_name}' is {item.price}")
            else:
                cont +=1
        else:
            print(f"Failed to retrieve price for '{market_hash_name}'.")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")


# Load data from JSON file
with open('skins.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

# List to store all item objects
items = []
cont = 0
# Iterate over each skin and create Item objects
for item_data in data:
    tid = item_data.get('id')
    tname = item_data.get('name')
    tweapon = item_data.get('weapon')
    tcategory = item_data.get('category')
    tpattern = item_data.get('pattern')
    tmin_float = item_data.get('min_float')
    tmax_float = item_data.get('max_float')
    trarity = item_data.get('rarity')
    tstattrak = item_data.get('stattrak')
    tsouvenir = item_data.get('souvenir')
    tpaint_index = item_data.get('paint_index')
    twears = item_data.get('wears')
    tcollections = item_data.get('collections')

    if tcategory['name'] != "Knives" and tcategory['name'] != "Gloves":

        for wear in twears:
            items.append(Item(tid, tname, tweapon, tcategory, tpattern, tmin_float, tmax_float, trarity, tpaint_index, wear, tcollections))
            get_median_price(items[-1], cont)
            print(len(items)-1)
            wait_random_time()

z = 0
# Display all items
print("Errors:", cont)
get_median_price(items[0])
print("Price:", items[0].price)

with open("items.pkl", "wb") as f:
    pickle.dump(items, f)



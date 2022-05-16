import json
import copy

# List of dictionaries
inventory = []
num_items = 0

with open("inventory_data.json") as f:
    data = json.load(f)

    for item in data["inventory"]:
        inventory.append(copy.deepcopy(item))
        num_items += 1

print("Loaded JSON data")

print(inventory)
print(num_items)







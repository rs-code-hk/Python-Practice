banned_items = ["slingshot","laser"]
inventory = ["apple","slingshot","book","laser"]
confiscated = []
print(f"Scanning inventory: {", ".join(inventory)}")
for item in inventory:
    if item in banned_items:
        print(f"Alert! Found banned item: {item}")
        confiscated.append(item)
        inventory.remove(item)
print(f"Scan complete. Total flag matches: {len(banned_items)}")
if len(confiscated) > 0:
    print("Items confiscated:")
    for i, j in enumerate(confiscated):
        print(f"{i+1}: {j}")
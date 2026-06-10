VIP_ROOM = "101"
guests = ["Alice","Bob"]
print(f"Current guests: {guests}")
new_guest = input("Enter name of new guest: ")
guests.append(new_guest)
print(f"The first guest registered is: {guests[0]}")
search_name = input("Search for a guest name to checkout: ")
index = 0
while index < 2:
    if guests[index] == search_name:
        guests.remove(search_name)
        break
    index = index + 1

# POP the last remaining guest out of the list and store it in a variable called departed_guest
# PRINT "Departed: " concatenated with departed_guest.
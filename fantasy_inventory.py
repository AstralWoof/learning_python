# Day 1 of code
# 7/7/21
# Fantasy inventory Version 1.0
# list to dictonary
# this project was a sum of everthing i reviewed today
# basic data type, flow control,data structure
# will show the current items in dict
def displayInv(inv):
    # will loop through items which comes as ordered pair (k,v)
    for key , value in inv.items():
        print(f"{key} : {value}")

# Find how many items are in the inventory
def totalOfInv(inv):
    count = 0
    # will loop through just the values in a dict then add them together
    for value in inv.values():
        count += value
    print(f"Items in inventory: {count}")
# will convert a list of items and add them to a dict
def addToinv(inv, loot):
    # grab each name in loot list
    for name in loot:
        if inv.get(name,0) ==0: # if items is not in my dict them add it by using key and set a defult values
            inv[name] = 1
        else:
            inv[name]+=1 # if items is already in dict increment it by 1
    print("inventory has been updated....")
my_inv = {"Sword of slaying": 1, "gold coin": 69, "rope":6, "tent": 2}
dragonLoot = ["gold coin", "Dragon Sword Of Fire", "Amulet of Lost","Dragon scales","gold coin"]

displayInv(my_inv)
totalOfInv(my_inv)
addToinv(my_inv,dragonLoot)
displayInv(my_inv)
totalOfInv(my_inv)
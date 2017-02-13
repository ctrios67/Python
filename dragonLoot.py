dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
player1 = {'rope': 1,
           'torch': 6,
           'gold coin': 42,
           'dagger': 1,
           'arrow': 30}

def displayInventory(playerInv):
    item_total = 0
    print("Inventory:")
    for k in playerInv.keys():
        item_total = item_total + playerInv.get(k,0)
        print(str(k) + 's ' + str(playerInv.get(k,0)))
    print("Total number of items: " + str(item_total))

def addToInventory(playerInv, loot):
    itemcount = 0
    for k in range(len(dragonLoot)):
        lootItem = dragonLoot[k]
        if(lootItem in playerInv): #    This only handles items already had
            playerInv[lootItem] = playerInv[lootItem] + 1
        else:
            playerInv.setdefault(dragonLoot[k],1)
    return playerInv

print("Player loot before battle with dragon.")
displayInventory(player1)

inv = addToInventory(player1, dragonLoot)

print("\nPlayer loot after dragon is slain.\n")

displayInventory(inv)

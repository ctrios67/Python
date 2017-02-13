def displayInventory(playerInv):
    item_total = 0
    print("Inventory:")
    for k in playerInv.keys():
        item_total = item_total + playerInv.get(k,0)
        print(str(k) + 's ' + str(playerInv.get(k,0)))
    print("Total number of items: " + str(item_total))

player1 = {'rope': 1,
           'torch': 6,
           'gold coin': 42,
           'dagger': 1,
           'arrow': 30}

displayInventory(player1)

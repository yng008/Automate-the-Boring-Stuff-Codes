def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inv.setdefault(addedItems[i], 0)
        inv[addedItems[i]] = inv[addedItems[i]]+ 1

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(v, k)
    print("Total number of items: " + str(item_total))
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

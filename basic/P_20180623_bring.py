stuff={'rope':1,'torch':3,'gold coin':15,'dagger':1,'arrow':50}

def display_inventory(inverntory):
    print('Inventory:')
    item_total=0
    for k,v in inverntory.items():
        print(str(v)+' '+k)
        item_total+=v
    print('Total number of items:'+str(item_total))

display_inventory(stuff)

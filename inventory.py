def invent(strength, hpp, inventory):
    item = input('What do you want  to use:')
    if (item.lower()).strip() == 'strengthpotion' or item.lower() == 'strength' or (item.lower()).strip() == 'strength potion':
        item = 'Strength Potion'
        if item in inventory:
            strength +=2
            inventory.remove(item)
            print(f'System: Your strength💪🏼 has increased to {strength}')
        else:
            print('System: Not enough resources ! ＞﹏＜')
    elif (item.lower()).strip() == 'healthpotion' or item.lower() == 'health' or (item.lower()).strip() == 'health potion':
        item = 'Health Potion'
        if item in inventory:
            hpp += 5
            inventory.remove(item)
            print(f'System: Your HP has increased to {hpp}')
        else:
            print('System: Not enough resources ! ＞﹏＜')
    return strength, hpp, inventory

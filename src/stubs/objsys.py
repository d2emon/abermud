from .support import Item


def iscontin(state, o1, o2):
    item1 = Item(state, o1)
    item2 = Item(state, o2)
    if item1.carry_flag != Item.CONTAINED_IN:
        return False
    if oloc(item1.item_id) != item2.item_id:
        return False
    if state['my_lev'] < 10 and isdest(item1.item_id):
        return False
    return True


def ishere(state, item_id):
    item = Item(state, item_id)
    if state['my_lev'] < 10 and isdest(item.item_id):
        return False
    if item.carry_flag == Item.CARRIED_BY:
        return False
    if oloc(item.item_id) != state['curch']:
        return False
    return True


def iscarrby(state, item_id, player_id):
    item = Item(state, item_id)
    if state['my_lev'] < 10 and isdest(item.item_id):
        return False
    if item.carry_flag not in (Item.CARRIED_BY, Item.WORN_BY):
        return False
    if oloc(item.item_id) != player_id:
        return False
    return True

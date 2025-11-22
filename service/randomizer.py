import random
from config.models import Item

def random_hero(heroes: list[str]):
    return random.choice(heroes)

def random_item(items: list[Item]):
    itemsDict = {}
    for item in items:
        itemsDict[item.category] = []

    for item in items:
        itemsDict[item.category].append(item)

    items: list[Item] = []
    for category in itemsDict.values():
        randItem: Item = random.choice(category)
        partsOf = []
        for x in items:
            partsOf += x.partOf
        while randItem.name in partsOf:
            randItem = random.choice(category)
        items.append(randItem)

    return [x.name for x in items]
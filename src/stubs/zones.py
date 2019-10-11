"""
Zone based name generator
"""
class Zone:
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc


state = {
    'zoname': [
        Zone("LIMBO", 1),
        Zone("WSTORE", 2),
        Zone("HOME", 4),
        Zone("START", 5),
        Zone("PIT", 6),
        Zone("WIZROOM", 19),
        Zone("DEAD", 99),
        Zone("BLIZZARD", 299),
        Zone("CAVE", 399),
        Zone("LABRNTH", 499),
        Zone("FOREST", 599),
        Zone("VALLEY", 699),
        Zone("MOOR", 799),
        Zone("ISLAND", 899),
        Zone("SEA", 999),
        Zone("RIVER", 1049),
        Zone("CASTLE", 1069),
        Zone("TOWER", 1099),
        Zone("HUT", 1101),
        Zone("TREEHOUSE", 1105),
        Zone("QUARRY", 2199),
        Zone("LEDGE", 2299),
        Zone("INTREE", 2499),
        Zone("WASTE", 99999),
    ],
    'ex_dat': [0] * 7,
    'dirns': [
        "North",
        "East ",
        "South",
        "West ",
        "Up   ",
        "Down ",
    ]
}


def findzone(x, __str):
    raise NotImplementedError()


def exits():
    raise NotImplementedError()


def lodex(file):
    raise NotImplementedError()


def roomnum(__str, offset):
    raise NotImplementedError()


def showname(loc):
    raise NotImplementedError()


def loccom():
    raise NotImplementedError()

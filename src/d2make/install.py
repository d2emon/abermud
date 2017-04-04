from dummysh import cp


def install2():
    print('Compiling world maker')
    w = [
        "makeworld",
        "blib",
    ]
    print("--->", w)
    print("--->\t./makeworld.util")
    print('Game universe intialised')
    print('Compiling reset data compiler')
    w = [
        "ogen",
        "blib",
    ]
    print("--->", w)
    print("--->\t./ogenerate")
    cp("ob.out", "reset_data")
    print('Reset data generated')
    print('Compiling uaf generator')
    w = [
        "makeuaf",
    ]
    print("--->", w)
    print("--->\t./makeuaf >uaf.rand")
    print('Ok')
    print('Now set up a password for arthur the archwizard')
# from d2lib import cuserid
from mud.utils import cls, crapup
from config import CONFIG
from run_game import main


def execl(filename, title, user, id):
    print("CONFIG{EXE}", CONFIG['EXE'])
    print("{}\n{}{}::{}".format(filename, title, user, id))
    return -1


def enter_game(user):
    cls()
    print("The Hallway")
    print("You stand in a long dark hallway, which echoes to the tread of your")
    print("booted feet. You stride on down the hall, choose your masque and enter the")
    print("worlds beyond the known......\n")
    main("   --{----- ABERMUD -----}--    Playing as ", user, 0)
    crapup("mud.exe: Not Found")


def change_password(user):
    print("--->\tchpwd({})".format(user))


def test_game(user):
    # if not user.isawiz:
    #    return
    cls()
    print("Entering Test Version")


def show_user(user):
    # if not user.isawiz:
    #    return
    print("--->\tshowuser({})".format(user))


def edit_user(user):
    # if not user.isawiz:
    #    return
    print("--->\tedituser({})".format(user))


def del_user(user):
    # if not user.isawiz:
    #    return
    print("--->\tdeluser({})".format(user))


def exit_mud(user):
    import sys
    sys.exit(0)


def talker(user):
    menu_items = {
        '1': enter_game,
        '2': change_password,
        '0': exit_mud,
        '4': test_game,
        'a': show_user,
        'b': edit_user,
        'c': del_user,
    }
    print("QNMRQ", user.qnmrq)
    if user.qnmrq:
        if main("   --}----- ABERMUD -----{--    Playing as ", user, 0) == -1:
            crapup("mud.exe : Not found")
    cls()
    while True:
        print("Welcome To AberMUD II [Unix]\n\n")
        print("Options\n")
        print("1]  Enter The Game")
        print("2]  Change Password")
        print("\n\n")
        print("0] Exit AberMUD")
        print("\n")
        isawiz = False
        if user.id in [1, ]:
            print("4] Run TEST game")
            print("A] Show persona")
            print("B] Edit persona")
            print("C] Delete persona")
            isawiz = True
        print("\n\n")
        # l2:
        answer = input("Select > ").lower()
        action = menu_items.get(answer)
        if action is None:
            print("Bad Option")
        else:
            action(user)

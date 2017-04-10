# from d2lib import cuserid
from mud.utils import cls, crapup
from game import main
from getpass import getpass
from user.login import search, show, edit_field, change_password
from user.models import User


def enter_game(user, session=None):
    cls()
    print("The Hallway")
    print("You stand in a long dark hallway, which echoes to the tread of your")
    print("booted feet. You stride on down the hall, choose your masque and enter the")
    print("worlds beyond the known......\n")
    main("   --{----- ABERMUD -----}--    Playing as ", user)
    crapup("mud.exe: Not Found")


def change_my_password(user, session=None):
    import db
    engine, session = db.connect()
    change_password(user)


def test_game(user, session=None):
    if not user.isawiz:
        return
    cls()
    print("Entering Test Version")


def show_user(user, session=None):
    if not user.isawiz:
        return
    cls()
    username = search()
    show(username)
    getpass("\nHit Return...")


def edit_user(user, session=None):
    if not user.isawiz:
        return

    cls()
    username = search()
    shuser = show(username, session)
    if shuser is None:
        shuser = User(username)
    print("\nEditing : {}\n".format(username))
    try:
        shuser.username = edit_field("Name: ", shuser.username)
        shuser.password = edit_field("Password: ", shuser.password)
        shuser.save(session)
        print("{} saved".format(shuser.username))
    except AssertionError as e:
        print(e)
        print("Changes not saved")


def del_user(user, session=None):
    if not user.isawiz:
        return

    cls()
    username = search()
    shuser = show(username, session)
    if shuser is None:
        print("\nCannot delete non-existant user")
        return
    session.delete(shuser)
    session.commit()


def exit_mud(user):
    import sys
    sys.exit(0)


def talker(user):
    menu_items = {
        '1': enter_game,
        '2': change_my_password,
        '0': exit_mud,
        '4': test_game,
        'a': show_user,
        'b': edit_user,
        'c': del_user,
    }
    print("QNMRQ", user.qnmrq)
    if user.qnmrq:
        if main("   --}----- ABERMUD -----{--    Playing as ", user) == -1:
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
        if user.isawiz:
            print("4] Run TEST game")
            print("A] Show persona")
            print("B] Edit persona")
            print("C] Delete persona")
        print("\n\n")
        answer = input("Select > ").lower()
        action = menu_items.get(answer)
        if action is None:
            print("Bad Option")
        else:
            action(user)

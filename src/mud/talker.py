from d2lib import cuserid
from mud.utils import cls, crapup


def execl(filename, title, user, id):
    print("{}\n{}{}::{}".format(filename, title, user, id))
    return -1


def talker(user):
    while True:
        print("QNMRQ", user.qnmrq)
        if user.qnmrq:
            if execl('EXE', "   --}----- ABERMUD -----{--    Playing as ", user, 0) == -1:
                crapup("mud.exe : Not found")
        cls()
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
        if answer == '1':
            cls()
            print("The Hallway")
            print("You stand in a long dark hallway, which echoes to the tread of your")
            print("booted feet. You stride on down the hall, choose your masque and enter the")
            print("worlds beyond the known......\n")
            execl('EXE', "   --{----- ABERMUD -----}--    Playing as ", user, 0)
            crapup("mud.exe: Not Found")
        elif answer == '0':
            import sys
            sys.exit(0)
        else:
            print("Bad Option")

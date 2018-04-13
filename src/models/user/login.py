from config import CONFIG
from d2log import mud_logger as logger
from mud.views import cls
from .models import User
from getpass import getpass


def search():
    import db
    engine, session = db.connect()
    users = session.query(User).all()
    for u in users:
        print("{}:\t{}".format(u.id, u.username))
    return input("\nUser Name: ")


def show(username):
    user = User.by_username(username)
    if user is None:
        print("\nNo user registered in that name\n\n")
    else:
        print("\n\nUser Data For {}\n".format(user.username))
        print("Name: {}\nPassword: {}\n".format(user.username, user.password))
    return user


def edit_field(title, value):
    new_value = input("{}(Currently {}): ".format(title, value))

    if not new_value:
        new_value = value
    return new_value


def change_password(user):
    try:
        data = input_password("\nOld Password\n*\t")
        assert data == user.password, "Incorrect Password"
    except AssertionError as e:
        print(e)
        return

    while True:
        try:
            password = input_password("\nNew Password\n*\t")
            verify = input_password("\nVerify Password\n*\t")
            assert verify == password, "Passwords doesn't match"
            user.password = password
        except AssertionError as e:
            print(e)
            continue
        break
    user.save()
    print("Changed")
    return

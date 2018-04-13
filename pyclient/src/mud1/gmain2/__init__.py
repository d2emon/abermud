from .cli import cls, inputUser, loadUser, newUser

def login(username):
    username, user = inputUser(username)
    cls()
    print(username, user)
    if user is None:
        return newUser(username)
    else:
        return loadUser(username)


def talker(user):
    print(user)
    # return talker(user) // Run system

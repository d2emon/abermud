from mud.errors import LoginError


def askYN(prompt):
    answer = input(prompt).lower()
    return (not len(answer)) or (answer[0] != 'n')


def inputUsername(
    username='',
    prompt='By what name shall I call you?\n',
    callback=None,
):
    while True:
        print(username)
        if not username:
            username = input(prompt)
        try:
            if callback is None:
                return username
            return callback(username)
        except:
            username = ''
            continue


def inputPassword(
    username,
    prompt="*",
    callback=None,
    tries=3,
):
    while tries > 0:
        password = input(prompt)
        try:
            if callback is None:
                return password, None
            return password, callback(username, password)
        except:
            tries -= 1
            continue
    raise LoginError


def testUsername(username):
    user = findUser(username)

    print(user)
    data = user.get('user')
    if data or askYN('Did I get the name right %s?\n' % (username)):
        return username, data
    return inputUser(None)


def inputUser(username=None):
    return inputUsername(
        username,
        prompt='By what name shall I call you?\n',
        callback=testUsername
    )


def newUser(username=None):
    cls()
    print(username)
    # this bit registers the new user
    print("Creating new persona...")
    return inputPassword(
        username,
        prompt="Give me a password for this persona\n",
        callback=addUser,
    )


def loadUser(username=None):
    return inputPassword(
        username,
        prompt="This persona already exists, what is the password?\n",
        callback=login,
    )

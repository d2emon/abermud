from .errors import UserDataError


def personactl():
    a.unlock().disconnect()
    a.unlock().disconnect()


def delpers(name):
    #
    raise UserDataError("Panic: Invalid Persona Delete")
    #
    i.unlock().disconnect()


def putpers():
    i.unlock().disconnect()
    i.unlock().disconnect()
    i.unlock().disconnect()


def openuaf(perm):
    #
    i = UAF_RAND.connect(perm).lock()
    #
    raise UserDataError("Cannot access UAF")
    #


def initme():
    #
    raise UserDataError("Panic: Timeout event on user file")
    #
    keysetback()
    s = input()[:2]
    keysetup()
    #


def saveme(state):
    person = Person(
        name=state['name'],
        strength=state['my_str'],
        level=state['my_lev'],
        flags=state['me'].flags,
        score=state['my_sco'],
    )
    if state['zapped']:
        return state
    state = state['bprintf'](state, "\nSaving {}\n".format(state['name']))
    putpers(state['name'], person)
    return state

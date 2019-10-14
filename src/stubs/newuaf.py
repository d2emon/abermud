from .errors import UserDataError


def delpers(name):
    #
    raise UserDataError("Panic: Invalid Persona Delete")
    #


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

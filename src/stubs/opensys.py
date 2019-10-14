from .errors import WorldError


def openworld():
    #
    filrf = Service("/usr/tmp/-iy7AM").open('r+').lock()
    #
    raise WorldError("Cannot find World file")

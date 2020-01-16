import sys


def pbfr():
    raise NotImplementedError()


def set_pr_due(value):
    raise NotImplementedError()


class MudError(Exception):
    pass


__dashes = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"


def on_error(error):
    pbfr()
    set_pr_due(0)
    print("\n{dashes}\n{message}\n{dashes}".format(
        dashes=__dashes,
        message=str(error),
    ))
    sys.exit(0)

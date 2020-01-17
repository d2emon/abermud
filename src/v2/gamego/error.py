import sys


class MudError(Exception):
    pass


__dashes = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"


def on_error(player, error):
    player.show_messages()
    player.reset_pr_due()

    print("\n{dashes}\n{message}\n{dashes}".format(
        dashes=__dashes,
        message=str(error),
    ))
    sys.exit(0)

from bprintf import buff


PROGNAME = ""


def crapup(s):
    dashes = ("-="*76) + '-'
    buff.pbfr()
    buff.pr_due = False

    # So we dont get a prompt after the exit
    # keysetback();

    print()
    print(dashes)
    print("\n{}\n".format(s))
    print(dashes)

    import sys
    sys.exit(0)


def set_name(newname):
    global PROGNAME
    PROGNAME = newname

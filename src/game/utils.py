from bprintf import buff


def crapup(s):
    dashes = ("-="*76) + '-'
    buff.pbfr()
    pr_due = 0
    # So we dont get a prompt after the exit
    # keysetback();

    print()
    print(dashes)
    print("\n{}\n".format(s))
    print(dashes)

    import sys
    sys.exit(0)

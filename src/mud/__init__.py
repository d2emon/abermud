'''
Program starts Here!

This forms the main loop of the code, as well as calling
all the initialising pieces
'''


def main(*argv):
    import mud.run
    return mud.run.main(*argv)


if __name__ == "__main__":
    import sys
    main(*sys.argv)

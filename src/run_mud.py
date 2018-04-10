#! /usr/bin/env python
import mud


def main():
    # import logging
    # logformat = '\t%(levelname)s:%(name)s:%(message)s [in %(pathname)s:%(lineno)d]'
    # logging.basicConfig(format=logformat)
    # logging.basicConfig(level=logging.DEBUG, format=logformat)

    import sys
    mud.main(*sys.argv)


if __name__ == "__main__":
    main()

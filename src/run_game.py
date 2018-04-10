#! /usr/bin/env python
import game


def main(title='', user=None):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    import sys
    game.main(*sys.argv[1:])
    return 0


if __name__ == "__main__":
    main()

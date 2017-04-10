#! /usr/bin/env python
import mud


def main():
    import logging
    logging.basicConfig(level=logging.DEBUG)

    import sys
    mud.main(*sys.argv)


if __name__ == "__main__":
    main()

#! /usr/bin/env python
from mud import run
from d2log import mud_logger as logger, load_logger



def main():
    # import logging
    # logformat = '\t%(levelname)s:%(name)s:%(message)s [in %(pathname)s:%(lineno)d]'
    # logging.basicConfig(format=logformat)
    # logging.basicConfig(level=logging.DEBUG, format=logformat)
    pass


if __name__ == "__main__":
    load_logger(logger)

    import sys
    run.main(*sys.argv)

#! /usr/bin/env python
from dummysh import mkdir, clear_file
import d2make


def make_dirs():
    print('Making directories')
    mkdir("TEXT")
    mkdir("SNOOP")
    mkdir("EXAMINES")
    mkdir("TEXT/ROOMS")


def init_files():
    print('initialising files')
    clear_file("mud_syslog")
    clear_file("reset_t")
    clear_file("reset_n") 
    clear_file("user_file")

    
def main():
    make_dirs()
    init_files()
    d2make.compile_h()
    d2make.compile_mud_exe()
    d2make.compile_mud_1()
    print('Done')
    
    from d2make.install import install2
    install2()


if __name__ == "__main__":
    main()
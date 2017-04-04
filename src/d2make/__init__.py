from d2make import h_c
from d2make import exe
from d2make import mud


def compile_h():
    print('Compiling .h constructor')
    files = h_c.main()
    for k, v in files.items():        
        print("{}:\t#define\t{}\t\"{}\"".format("files.h", k, v))    
    print('.h built')


def compile_mud_exe():
    print('Compiling mud.exe')
    exe.main()

    
def compile_mud_1():
    print('Compiling mud.1')
    mud.main()
from d2make import h_c


def gcc_compiler(res):
    print(res)
    pass


def compile_h():
    print('Compiling .h constructor')
    files = h_c.main()
    for k, v in files.items():
        print("{}:\t#define\t{}\t\"{}\"".format("files.h", k, v))
    print('.h built')

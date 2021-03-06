'''
B functions and utilities
'''


def scan(v_out, v_in, v_start, v_skips, v_stops):
    if len(v_in) < v_start:
        return '', -1
    i = v_start
    while i < len(v_in) and (v_in[i] in v_skips):
        i += 1
    if not v_in[i:]:
        return '', -1
    while i < len(v_in) and (v_in[i] not in v_stops):
        v_out += v_in[i]
    return v_out, i


# char *getstr(file,st)
# void addchar(str,ch)
# long numarg(str)
# sbar()

# void f_listfl(name,file)
# void listfl(name)
def printfile(filename):
    # print("--->\tlistfl(\"{}\")".format(filename))
    print("\n")
    try:
        with open(filename) as a:
            s = a.read()
        print(s)
        print("\n")
    except:
        print("[Cannot find file -> {}]".format(filename))
        return
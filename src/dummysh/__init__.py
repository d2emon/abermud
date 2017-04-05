def mkdir(dirname):
    print("--->\tmkdir {}".format(dirname))

    
def clear_file(filename):
    print("--->\tcat </dev/null >{}".format(filename))
    
    
def cp(filename1, filename2):
    print("--->\tcp {} {}".format(filename1, filename2))
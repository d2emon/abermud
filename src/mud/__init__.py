import socket
import os
import config
from mud.utils import ttyt, getty, cls, validname, dcrypt
from d2lib import cuserid
from datetime import datetime, timedelta


# include "files.h"
# include <stdio.h>
# include <sys/types.h>
# include <sys/stat.h>
# include "System.h"


# char lump[256];
namegiv = False
namegt = None
qnmrq = False
FILES = dict()

'''
Program starts Here!

This forms the main loop of the code, as well as calling
all the initialising pieces
''' 

def elapsed():
    import humanize
    a = FILES["RESET_N"]
    try:
        with open(a) as f:
            d = yaml.load(f)
            r = d['started']
    except:
        return "AberMUD has yet to ever start!!!"

    dt = humanize.naturaltime(datetime.now() - r)
    return "Game time elapsed: {}".format(dt)
    

def main(*argv):
    '''
    The initial routine
    '''
    global FILES
    FILES = config.load()
    
    namegiv = False
    namegt = ""
    qnmrq = False
    # FILE *a;

    # Check we are running on the correct host
    # see the notes about the use of flock();
    # and the affects of lockf();
    user = socket.gethostname()
    if user != FILES["HOST_MACHINE"]:
        raise Exception("AberMUD is only available on {}, not on {}".format(FILES["HOST_MACHINE"], user))
    b = [0, 0, 0]

    # Check if there is a no logins file active
    print("\n\n\n\n")
    chknolog()
    if len(argv) > 1:
        arg = argv[1].upper()
    else:
        arg = ' '
    
    if arg[0] == '-':
        # Now check the option entries
        # -n(name)
        key = arg[1]
        if key == 'N':
            qnmrq = True
            ttyt = 0
            namegt = arg[2:]
            namegiv = True
        else:
            getty()
    else:
        getty()
    
    num = 0
    # Check for all the created at stuff
    # We use stats for this which is a UN*X system call
    if not namegiv:
        print(FILES["EXE"])
        cls()

        try:
            space = os.path.getmtime(FILES["EXE"])
            space = datetime.fromtimestamp(space).strftime("%x %X")
        except:
            space = "<unknown>"
        ta = elapsed()
        
        print("""
                         A B E R  M U D
        
                  By Alan Cox, Richard Acott Jim Finnis
                  
        This AberMUD was created: {}
        {}
        """.format(space, ta))
    login(namegt)
    # Does all the login stuff
    if not qnmrq:
        cls()
        # listfl(MOTD);             /* list the message of the day */
        space = input("399")
        print("\n\n")
    space = cuserid()
    # syslog("Game entry by %s : UID %s",user,space); /* Log entry */
    # talker(user);                /* Run system */
    crapup("Bye Bye")  # Exit

 
# char usrnam[44];
 

def login(user):
    '''
    The whole login system is called from this
    '''
    def validate(user):
        try:
            return test_name(user)
        except ValueError as e:
            print(e)
            return False
        
    def test_name(user):
        print("--->\tvalidate({})".format(user))
        # Check for legality of names
        if not user:
            raise ValueError("Empty user name")

        if '.' in user:
            raise ValueError("Illegal characters in user name")

        user = user.strip()
        if ' ' in user:
            raise ValueError("Illegal characters in user name")

        if not chkname(user):
            raise ValueError("")

        if not validname(user):
            raise ValueError("Bye Bye")

        a = logscan(user)
        if a is None:
            # If he/she doesnt exist
            a = input("\nDid I get the name right {} ?".format(user)).lower()
            c = a[0]
            print("\n")
            return c == 'y'
            # Check name
        return True

    # Check if banned first
    b = chkbnid(cuserid())  # cuserid(NULL));
    print(b)
    
    namegiv = False
    while not validate(user):
        # Get the user name
        user = input("By what name shall I call you ?\n*")[:15]
        print("INPUT", user)
    logpass(user)  # Password checking
        

def chkbnid(user):
    '''
    Check to see if UID in banned list
    '''
    c = user.lower()
    a = ""  # openlock(BAN_FILE,"r+");
    if a is None:
        return False
    b = ''
    for b in a:
        if b == '\n':
            b = ''
        b = b.lower()
        if b == user:
            raise Exception("I'm sorry- that userid has been banned from the Game")
    # fclose(a);
    return False


def logscan(uid):
    '''
    Return block data for user or -1 if not exist
    '''
    print("UID", uid)
    import yaml
    # unit = openlock(PFL,"r")
    # if unit is None:
    #     raise Exception("No persona file")
    with open(FILES["PFL"]) as f:
        persons = yaml.load(f)
        # block = dcrypt(block)

    if persons is None:
        return None
    
    for p in persons:
        print(p['username'], uid)
        if p['username'].lower() == uid.lower():
            return p
    return None


def logpass(uid):
    '''
    Main login code
    '''
    block = logscan(uid)
    pwd = uid  # save for new user
    if block:
        tries = 3
        while tries:
            # pastry:
            pwd = input("\nThis persona already exists, what is the password ?\n*")
            # fflush(stdout)
            # gepass(block)
            print("\n")
            
            if block['password'] == pwd:
                return True
            
            tries -= 1
            if not tries:
                raise Exception("\nNo!\n\n")
    else:
        # this bit registers the new user
        print("Creating new persona...\n");
        print("Give me a password for this persona\n");
        while True:
            # repass:
            block = input("*")
            # fflush(stdout)
            # gepass(block)
            print("\n")
            if '.' in block:
                print("Illegal character in password\n")
                continue
            if block:
                break
        uid = pwd
        pwd = block
        block = {
            "username": uid,
            "password": pwd,
        }
        
        import yaml

        with open(FILES["PFL"]) as f:
            persons = yaml.load(f)

        if persons is None:
            persons = []

        persons.append(block)

        # unit = openlock(PFL,"a")
        # if unit is None:
        #     raise Exception("No persona file")
        with open(FILES["PFL"], "w") as f:
            # block = dcrypt(block)
            yaml.dump(persons, f)
    cls()
    return True


# void getunm(name)
# void showuser()
# long shu(name,block)  /* for show user and edit user */
# void deluser()
# void edituser()
# void ed_fld(name,string)
# void delu2(name)   /* For delete and edit */
#void chpwd(user)   /* Change your password */

# void listfl(name)


def crapup(ptr):
    input("\n{}\n\nHit Return to Continue...\n".format(ptr))

    import sys
    sys.exit(0)

 
def chkname(user):
    import re
    return re.match("^\w*$", user)


def chknolog():
    try:
        with open(FILES["NOLOGIN"]) as a:
            s = a.read()
        print(s)
    except:
        return

    import sys
    sys.exit(0)


if __name__ == "__main__":
    import sys
    main(*sys.argv)
from config import CONFIG
from game.sigs import init
from game.talker import talker


def main(*argv):
    run_data = {
        'filename': CONFIG['EXE'],
        'title': '<untitled>',
        'user': None,
    }

    print("ARGS:", argv)
    argv_p = argv
    assert len(argv) == 2, "Args!"
    if len(argv) > 0:
        run_data['title'] = argv[0]
    if len(argv) > 1:
        run_data['user'] = argv[1]
    print("RUN DATA: ", run_data)

    print("="*80)
    if run_data['user']:
        username = run_data['user'].username
    else:
        username = '<UNNAMED>'
    print(run_data['filename'])
    print("{}{}".format(run_data['title'], username))
    print("="*80)

    init()

    user = argv[1]
    assert user is not None, "User don't exists"

    print("Entering Game ....")
    tty = 0
    # if tty == 4:
        # initbbc()
        # initscr()
        # topscr()
    username = user.username.capitalize()
    if username == "Phantom":
        username = "The {}".format(username)
    print("Hello {}".format(username))
    # syslog("GAME ENTRY: %s[%s]",globme,cuserid(NULL))
    import logging
    logging.info("GAME ENTRY: {}[{}]".format(username, user.id))
    # keysetup();
    talker(user)


# char privs[4];

# listfl(name)
# char *getkbd(s,l)   /* Getstr() with length limit and filter ctrl */

# unblock_alarm()
# block_alarm()

# long interrupt=0;

# sig_alon()
# sig_occur()

# set_progname(n,text)

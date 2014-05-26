#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2014 МихалычЪ <МихалычЪ@PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import blib

#~ char **argv_p;

def main(username):
    from temp_aber import globme, tty
    
    import signals
    import key
    from talker import talker
    from support import syslog

    signals.init()
    if not username:
        raise Exception("Args!")
    print("Entering Game ...");
    tty=0;
    #~ if tty=4: initbbc(): initscr(): topscr()

    if username == "D2emon":
        globme = "The {0}".format(username)
    else:
        globme = username

    user_id = blib.cuserid()

    print("Hello {0}".format(globme))
    syslog("GAME ENTRY: {name}[{user_id}]".format(name=globme, user_id=user_id))
    key.setup()
    talker(globme)
    
    return 0

#~ char privs[4];

def crapup(str):
    """Quitting game with message"""
    import bprintf
    import key

    dashes = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    bprintf.pbfr()
    bprintf.pr_due = 0  
    #~ So we dont get a prompt after the exit
    key.setback()
    print("\n{0}\n\n{1}\n\n{0}\n".format(dashes, str))
    exit(0)
    
def listfl(name):
    """List file"""
    print(">>>listfl({0})".format(name))

def getkbd(s, l):
    """Getstr() with length limit and filter ctrl"""
    print(">>>getkbd({0}, {1})".format(s, l))

#~ long interrupt=0;

def set_progname(n,text):
    """Program name set"""
    print(">>>set_progname({0}, {1})".format(n,text))

if __name__ == '__main__':
    main("D2emon")


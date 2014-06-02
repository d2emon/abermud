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

import gamesys
from user import User

guser = 0

#~ char **argv_p;
#~ char privs[4];

def listfl(name):
    """List file"""
    print(">>>listfl({0})".format(name))

def getkbd(s, l):
    """Getstr() with length limit and filter ctrl"""
    print(">>>getkbd({0}, {1})".format(s, l))

def before_loop(username):
    """Setting up for main loop"""
    from temp_aber import maxu
    
    import gamesys
    import gamebuffer
    import signals
    import world
    import user
    import key

    global guser

    signals.init()
    guser = User(username)
    print("Entering Game ...");
    #~ WTF?
    tty=0;
    #~ if tty=4: initbbc(): initscr(): topscr()
    #~ WTF?
    guser.greeting()

    #~ Setting up game system
    key.setup()
    gamebuffer.makebfr()
    guser.msgId = -1

    guser.puton()

    #~ Some checks
    if not world.openw():
        raise Exception("Sorry AberMUD is currently unavailable")
        #~ Crapup
    if guser.userId >= maxu:
        raise Exception("Sorry AberMUD is full at the moment")
        #~ Crapup

    guser.name = username
    guser.chkMsg()
    
    world.closew()
    
    guser.msgId = -1
    guser.special(".g")
    #~ WTF?
    i_setup = 1

def main_loop(luser):
    """This file holds the basic communications routines"""
    from temp_talker import sendmsg, rd_qd

    import gamebuffer
    import world
    import user

    gamebuffer.pbfr()
    sendmsg(luser.name)
    if rd_qd:
        user.chkMsg(luser.name)
    rd_qd = False
    world.closew()
    gamebuffer.pbfr()

def main(username):
    import signals
    import user
    
    global guser

    before_loop(username)
    try:
        while True:
            main_loop(guser)
            signals.sloop()
    except KeyboardInterrupt:
        signals.ctrlc()
    
    return 0

if __name__ == '__main__':
    main("D2emon")


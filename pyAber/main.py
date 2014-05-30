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
    from temp_talker import cms, putmeon, mynum, rte, special
	
    import gamesys
    import gamebuffer
    import signals
    import world
    import user

    signals.init()
	user.ne
    print("Entering Game ...");
    tty=0;
    #~ if tty=4: initbbc(): initscr(): topscr()

    if username == "D2emon":
        user.username = "The {0}".format(username)
    else:
        user.username = username

    user_id = gamesys.cuserid()

    print("Hello {0}".format(user.username))
    gamesys.syslog("GAME ENTRY: {name}[{user_id}]".format(name=user.username, user_id=user_id))
    key.setup()

    gamebuffer.makebfr()
    cms = -1
    putmeon(username)
    if not world.openw():
        gamesys.crapup("Sorry AberMUD is currently unavailable")
        raise Exception("Sorry AberMUD is currently unavailable")
    if mynum >= maxu:
        gamesys.crapup("Sorry AberMUD is full at the moment")
        raise Exception("Sorry AberMUD is full at the moment")
    user.username = username
    rte(username)
    world.closew()
    cms= -1
    special(".g", username)
    i_setup = 1

def main_loop(username):
    """This file holds the basic communications routines"""
    from temp_talker import sendmsg, rd_qd, rte

    import gamebuffer
    import world

    gamebuffer.pbfr()
    sendmsg(username)
    if rd_qd:
        rte(username)
    rd_qd = False
    world.closew()
    gamebuffer.pbfr()

def main(username):
    import signals
    import user

    before_loop(username)
    try:
        while True:
            main_loop(user.username)
            signals.sloop()
    except KeyboardInterrupt:
        signals.ctrlc()
    
    return 0

if __name__ == '__main__':
    main("D2emon")


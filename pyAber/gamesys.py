#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gamesys.py
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

def crapup(str):
    """Quitting game with message"""
    import temp_bprintf
    import key

    dashes = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    temp_bprintf.pbfr()
    temp_bprintf.pr_due = 0  
    #~ So we dont get a prompt after the exit
    key.setback()
    print("\n{0}\n\n{1}\n\n{0}\n".format(dashes, str))
    exit(0)
    
def syslog(args):
    """Writing system log"""
    from temp_talker import loseme

    import config
    from datetime import datetime

    z = datetime.now()
    
    log_str = "{time}: {str}".format(time=z.strftime("%y.%m.%d %H:%M:%S"), str=args)

    with open(config.LOG_FILE, 'a') as x:
        if not x:
            loseme()
            raise Exception("Log fault")
        x.write(log_str+"\n")
    print("<--{0}".format(log_str) )

def cuserid():
    """Get user ID"""
    user_id = "192.168.0.78"
    return user_id
    pass
    
def main():
    """System functions"""
    print("Game system functions")
    return 0

if __name__ == '__main__':
    main()


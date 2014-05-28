#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gamebuffer.py
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

import signals

iskb   = True
#~ Are we showing text on screen?
pr_qcr = False
#~ Need we put a linebreak?
pr_due = False
#~ Need we show keyboar buffer?
sysbuf = ""
#~ System buffer

def makebfr():
    """Make system buffer"""
    global sysbuf
    sysbuf = ""

def pbfr():
    """Put buffer on screen"""
    from temp_aber import pname
    from temp_bprintf import log_fl, dcprnt

    import world
    import snoop
    
    global sysbuf, pr_due, pr_qcr, iskb

    signals.block_alarm()
    world.closew()
    if sysbuf:
        pr_due = True
    if sysbuf and pr_qcr:
        print("\n")
    pr_qcr = False
    if log_fl:
        iskb = False
        dcprnt(sysbuf, log_fl)
    if snoop.snoopd != -1:
        fln=snoop.opens(pname(snoop.snoopd),"a")
        if fln:
            iskb = False
            dcprnt(sysbuf,fln)
            #~ fcloselock(fln)
    iskb = True
    dcprnt(sysbuf, "stdout")
    sysbuf = ""
    #~ clear buffer
    if snoop.snoopt != -1:
        snoop.views()
    signals.unblock_alarm()


def main():
    """Functions to work with buffer"""
    printf("Buffer functions")
    return 0

if __name__ == '__main__':
    main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  без имени.py
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

tty = 0
maxu = 15
zapped = False

my_str = 0
my_lev = 0
my_sex = 0

debug_mode = True
convflg    = 0

in_fight = 0
fighting = 0

def gamecom(name):
	"""TODO : Game commands"""
	print(">>>gamecom({0})".format(name))

def update(name):
	"""TODO : Update data"""
	print(">>>update({0})".format(name))

def eorte():
	"""TODO : End of rte"""
	print(">>>eorte()")

def on_timing():
	"""TODO : On timing event"""
	print(">>>on_timing()")

def trapch(ch):
    """TODO : Go to room"""
    print(">>>trapch({0})".format(ch))

def randperc():
    """TODO : Random percent"""
    print(">>>randperc()")
    return 25

def cuserid():
    """TODO : User ID"""
    print(">>>cuserid()")

def initme():
    """TODO : Initialize player"""
    print(">>>initme()")

def sendsys(player_from, player_to, code, txt, block):
    """TODO : Send block"""
    print(">>>sendsys({0}, {1}, {2}, {3}, {4})".format(player_from, player_to, code, txt, block))

def readmsg(unit, block, ct):
    """TODO : Read messages"""
    print(">>>readmsg({0}, {1}, {2})".format(unit, block, ct))
	
def mstoout(block, name):
    """TODO : Show messages"""
    print(">>>mstoout({0}, {1})".format(block, name))

def fpbn(name):
    """TODO : Find player by name"""
    print(">>>fpbn({0})".format(name))
    return -1

def dumpitems():
    """TODO : Dump player items"""
    print(">>>dumpitems()")

def saveme():
    """TODO : Save player"""
    print(">>>saveme()")

def chksnp():
    """TODO : Check snoop"""
    print(">>>chksnp()")
    
def main():
    """Temporary functions"""
    return 0

if __name__ == '__main__':
    main()


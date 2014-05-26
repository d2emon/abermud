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

globme = ""
tty = 0
in_fight = 0
maxu = 15
zapped = False

my_str = 0
my_lev = 0
my_sex = 0

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

def sendmsg(name):
    """TODO : Send messages"""
    print(">>>sendmsg({0})".format(name))

def readmsg(unit, block, ct):
    """TODO : Read messages"""
    print(">>>readmsg({0}, {1}, {2})".format(unit, block, ct))
	
def mstoout(block, name):
    """TODO : Show messages"""
    print(">>>mstoout({0}, {1})".format(block, name))

def findend(unit):
    """TODO : Find end of messages"""
    print(">>>findend({0})".format(unit))
    return 10

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
    
def pvis(mynum):
    """TODO : Player visibility"""
    print(">>>pvis({0})".format(mynum))
    return 0

def pname(mynum):
    """TODO : Player name"""
    print(">>>pname({0})".format(mynum))
    return ""

def setpname(ct, value):
    """TODO : Set player name"""
    print(">>>setpname({0}, {1})".format(ct, value))

def setploc(ct, value):
    """TODO : Set player location"""
    print(">>>setploc({0}, {1})".format(ct, value))

def setppos(ct, value):
    """TODO : Set player position"""
    print(">>>setppos({0}, {1})".format(ct, value))

def setplev(ct,value):
    """TODO : Set player level"""
    print(">>>setplev({0}, {1})".format(ct, value))

def setpvis(ct,value):
    """TODO : Set player visibility"""
    print(">>>setpvis({0}, {1})".format(ct, value))

def setpstr(ct,value):
    """TODO : Set player strength"""
    print(">>>setpstr({0}, {1})".format(ct, value))

def setpwpn(ct,value):
    """TODO : Set player weapon"""
    print(">>>setpwpn({0}, {1})".format(ct, value))

def setpsex(ct,value):
    """TODO : Set player sex"""
    print(">>>setpsex({0}, {1})".format(ct, value))

def setpsexall(ct,value):
    """TODO : Set player flags"""
    print(">>>setpsexall({0}, {1})".format(ct, value))

def setphelping(ct,value):
    """TODO : Set player helping"""
    print(">>>setphelping({0}, {1})".format(ct, value))
    
def openworld():
    """TODO : Open world"""
    print("<-<openworld()")
    return True
    
def closeworld():
    """TODO : Close world"""
    print(">->closeworld()")
    
def rte(name):
    """TODO : Read messages"""
    print(">>>rte({0})".format(name))
    
def main():
    """Temporary functions"""
    return 0

if __name__ == '__main__':
    main()


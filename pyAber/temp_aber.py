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

def syslog(text):
    """TODO : System log"""
    print("syslog({0})".format(text))

def keysetup():
    """TODO : Key setup"""
    print("keysetup()")

def talker(globme):
    """TODO : Main loop"""
    print("talker({0})".format(globme))
    try:
        while True:
            pass
    except KeyboardInterrupt:
        from main import sig_ctrlc
        sig_ctrlc()

def cuserid():
	"""TODO : User ID"""
	print("cuserid()")

def loseme():
    """TODO : Losing game"""
    print("loseme()")

def crapup(text):
    """TODO : Showing final message"""
    print("crapup({0})".format(text))
    exit()

def keysetback():
    """TODO : Key return"""
    print("keysetback()")

def main():
	"""Temporary functions"""
	return 0

if __name__ == '__main__':
	main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  key.py
#  
#  Copyright 2014 МихалычЪ <d2emon@mikhalych-desktop>
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

#~ #include <stdio.h>
#~ #include <termios.h>

#~ long save_flag= -1;

def setup():
    """Setting up keys"""
    #~ struct termios ios;
    #~ tcgetattr(fileno(stdin),&ios);
    #~ save_flag=ios.c_lflag;
    #~ ios.c_lflag&=~(ECHO|ICANON);
    #~ tcsetattr(fileno(stdin),TCSANOW,&ios);
    print("-->keysetup()")
    pass

def setback():
    """Setting keys back"""
    #~ struct termios ios;
    #~ tcgetattr(fileno(stdin),&ios);
    #~ ios.c_lflag=save_flag;
    #~ tcsetattr(fileno(stdin),TCSANOW,&ios);
    print("-->keysetback()")
    pass

#~ char key_buff[256];
#~ char pr_bf[32];
#~ long key_mode= -1;

#~ key_input(ppt,len_max)

#~ key_reprint()

def main():
    """Working with keyboard"""
    print("Key drivers")
    return 0

if __name__ == '__main__':
    main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  key.py
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

buff  = ""
pr_bf = "PR"     # ""
mode  = -1

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

def reprint():
    """Reprint"""
    import gamebuffer

    global mode, pr_bf, buff

    gamebuffer.pr_qcr = True
    gamebuffer.pbfr()
    if not mode and gamebuffer.pr_due:
        print("\n{0}{1}", pr_bf, buff)
    gamebuffer.pr_due = False
	#~ fflush(stdout);

def prmpt(vis, debug, wiz, convflg):
    """Get prompt symbol"""
    p = "\r"
    if vis:
        p += "("

    if debug:
        p += "#"
    if wiz:
        p += "----"

    if convflg == 0:
        p += ">"
    elif convflg == 1:
        p += "\""
    elif convflg == 2:
        p += "*"
    else:
        p += "?"

    if vis:
        p += ")"

    return p

def kinput(ppt,len_max):
    """Input from keyboard"""
    #~ extern long pr_due;

    import gamebuffer

    global mode, buff
    
    x       = ""
    len_cur = 0
    mode    = 0

    pr_bf = ppt
    print(ppt)
    gamebuffer.pbfr()
    gamebuffer.pr_due = 0

    buff = ""
    
    while len_cur < len_max:
        #~ x = getchar()
        if x == "\n":
            print("\n")
            mode = 1
            return 0
        #~ if ((x == 8) or (x == 127)) and len_cur:
            #~ putchar(8);
            #~ putchar(' ');
            #~ putchar(8);
            #~ len_cur -= 1
            #~ buff[len_cur] = 0
            #~ continue
        #~ if x<32:
            #~ continue
        #~ if x==127:
            #~ continue
        #~ putchar(x)
        #~ buff[len_cur] = x
        #~ len_cur += 1
        #~ buff[len_cur] = 0
    print(">>>input(\n{0}, {1})".format(n, t))

def main():
    """Working with keyboard"""
    print("Key drivers")
    return 0

if __name__ == '__main__':
    main()


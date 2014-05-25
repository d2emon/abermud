#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bprintf.py
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

#~ #include "files.h"
#~ #include <stdio.h>
#~ #include "System.h"

pr_due = False

#~ void bprintf(args,arg1,arg2,arg3,arg4,arg5,arg6,arg7)

#~ The main loop

#~ void dcprnt(str,file)

#~ int pfile(str,ct,file)

#~ int pndeaf(str,ct,file)

 #~ pcansee(str,ct,file)

 #~ prname(str,ct,file)

#~ int pndark(str,ct,file)

#~ int tocontinue(str,ct,x,mx)

#~ int seeplayer(x)

#~ int ppndeaf(str,ct,file)

#~ int  ppnblind(str,ct,file)

sysbuf=""

def makebfr():
    """Make system buffer"""
    sysbuf = ""

#~ FILE * log_fl= 0; /* 0 = not logging */

#~ void logcom()

pr_qcr = False

def pbfr():
    """Put buffer on screen"""
    from temp_aber import closeworld
    from main import block_alarm, unblock_alarm
    #~ FILE *fln;
    #~ long mu;

    block_alarm()
    closeworld()
    if sysbuf:
        pr_due = True
    if sysbuf and pr_qcr:
        pass
        #~ putchar('\n');
    pr_qcr = False
    #~ if(log_fl!=NULL):
        #~ iskb=0;
        #~ dcprnt(sysbuf,log_fl);
    #~ if(snoopd!=-1):
        #~ fln=opensnoop(pname(snoopd),"a");
        #~ if(fln>0):
            #~ iskb = 0
            #~ dcprnt(sysbuf,fln);
            #~ fcloselock(fln);
    iskb = 1
    #~ dcprnt(sysbuf,stdout);
    sysbuf = "" #~ clear buffer
    #~ if(snoopt!=-1):
        #~ viewsnoop();
    unblock_alarm()

iskb = 1

#~ void quprnt(x)

#~ int pnotkb(str,ct,file)

#~ long snoopd= -1;

#~ FILE *opensnoop(user,per)

#~ long snoopt= -1;

#~ char sntn[32];

#~ void snoopcom()

#~ void viewsnoop()

#~ void chksnp()

#~ void setname(x)  /* Assign Him her etc according to who it is */

def main():
    """Buffered output"""
    print("Buffered functions")
    return 0

if __name__ == '__main__':
    main()


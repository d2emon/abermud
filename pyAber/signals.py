#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  signals.py
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

#~ import signal
import atexit

active = False
sigs   = {}
alarm  = 0

def block_alarm():
    """Block alarm"""
    #~ signal(SIGALRM,SIG_IGN);
    sigs['alrm'] = 0
    print(sigs)

def unblock_alarm():
    """Unblock alarm"""
	#~ signal(SIGALRM,sig_occur);
    sigs['alrm'] = 'sig_occur'
    print(sigs)
    if active:
        alarm = 2
        #~ alarm(2)

def alon():
    """Set signals on"""
    active = True   
	#~ signal(SIGALRM,sig_occur);
    sigs['alrm'] = 'sig_occur'
    print(sigs)
    alarm = 2
    #~ alarm(2)

def aloff():
    """Stopping signals"""
    active = False   
    #~ signal(SIGALRM,SIG_IGN);
    sigs['alrm'] = 0
    print(sigs)
    alarm = 2147487643
    #~ alarm(2147487643)

def init():
    "Initialization if signals"
    atexit.register(oops)
    
    #~ signal(SIGHUP,sig_oops);
    #~ signal(SIGINT,sig_ctrlc);
    #~ signal(SIGTERM,sig_ctrlc);
    #~ signal(SIGTSTP,SIG_IGN);
    #~ signal(SIGQUIT,SIG_IGN);
    #~ signal(SIGCONT,sig_oops);
    sigs['hup']  = 'oops'
    sigs['int']  = 'ctrlc'
    sigs['term'] = 'ctrlc'
    sigs['tstp'] = 0
    sigs['quit'] = 0
    sigs['cont'] = 'oops'
    print(sigs)

def occur():
    """Signal occured"""
    print(">>>sig_occur()")

def oops():
    "Quitting"
    from temp_aber import globme

    import key
    from talker import loseme

    aloff();
    loseme(globme);
    key.setback();
    print("Ooops")

def ctrlc():
    "Quitting on Ctrl+C"
    from temp_aber import in_fight

    from talker import loseme
    from main import crapup

    if in_fight:
        return

    atexit.unregister(sig_oops)
    aloff()
    loseme()
    crapup("Byeeeeeeeeee  ...........")

def main():
    """Functions to work with signals"""
    print("Functions to work with signals")
    return 0

if __name__ == '__main__':
	main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  support.py
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

#~ #include "object.h"
#~ #include <stdio.h>
#~ #include "files.h"

#~ extern FILE* openlock();
#~ extern OBJECT objects[];

#~ ocarrf(ob)

#~ setocarrf(ob,v)

#~ oloc(ob)

#~ setoloc(ob,l,c)

#~ ploc(chr)

#~ char * pname(chr)

#~ plev(chr)

#~ setplev(chr,v)

#~ pchan(chr)

#~ pstr(chr)

#~ setpstr(chr,v)

#~ pvis(chr)

#~ setpvis(chr,v)

#~ psex(chr)

#~ setpsex(chr,v)

#~ setpsexall(chr,v)

#~ psexall(chr)

#~ char * oname(ob)

#~ char * olongt(ob,st)

#~ omaxstate(ob)

#~ obflannel(ob)  /* Old version */

#~ oflannel(ob)

#~ obaseval(ob)

#~ isdest(ob)

#~ isavl(ob)

#~ ospare(ob)

#~ ppos(chr)

#~ setppos(chr,v)

#~ setploc(chr,n)

#~ pwpn(chr)

#~ setpwpn(chr,n)

#~ ocreate(ob)

#~ osetbit(ob,x)

#~ oclearbit(ob,x)

#~ oclrbit(ob,x)

#~ otstbit(ob,x)

#~ osetbyte(o,x,y)

#~ obyte(o,x)

#~ ohany(mask)

#~ phelping(x,y)

#~ setphelping(x,y)

#~ ptothlp(pl)

#~ psetflg(ch,x)

#~ pclrflg(ch,x)

#~ Pflags
#~ 
#~ 0 sex
#~ 1 May not be exorcised ok
#~ 2 May change pflags ok
#~ 3 May use rmedit ok
#~ 4 May use debugmode ok
#~ 5 May use patch 
#~ 6 May be snooped upon

#~ ptstbit(ch,x)

#~ ptstflg(ch,x)

def main():
    """Some more basic functions
    Note

    state(obj)
    setstate(obj,val)
    destroy(obj)

    are elsewhere
    """
    print("Functions for support")
    return 0

if __name__ == '__main__':
    main()


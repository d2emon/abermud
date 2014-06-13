#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  user.py
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

class User:
    name = ""
    
    msgId  = -1
    userId = 0
    locId  = -5
    data   = ["", 1, 2, 3, -4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    #~ ublock[16*chr+4]

    def __init__(this, newname):
        """Set user name"""
        if not newname:
            raise Exception("Args!")
            
        if newname == "D2emon":
            name = "The {0}".format(newname)
        else:
            name = newname        

    def getComputer(this):
        """Get user computer ID"""
        comp_id = "192.168.0.78"
        return comp_id

    def greeting(this):
        """Show greeting string"""
        import gamesys
        
        print("Hello {0}".format(this.name))
        gamesys.syslog("GAME ENTRY: {name}[{user_id}]".format(name=this.name, user_id=this.getComputer()))

    def puton(this):
        """Put user on"""
        from temp_aber import fpbn
        from temp_aber import maxu
        from temp_talker import iamon

        import gamesys
        import world

        #~ WTF?
        iamon = False

        unit  = world.openw()

        #~ If user is olready logged in
        if fpbn(this.name)!= -1:
            raise Exception("You are already on the system - you may only be on once at a time")
            #~ Crapup

        i = 0
        for i in range(0, maxu+1):
            #~ Get i user 
            if not this.getName():
                break

        this.userId = i
        if this.userId == maxu:
            return False

        this.setName(this.name)
        this.setLoc(this.locId)
        this.setPos(-1)
        this.setLev( 1)
        this.setVis( 0)
        this.setStr(-1)
        this.setWpn(-1)
        this.setSex( 0)

        #~ WTF?
        iamon = True
        return iamon    
        
    def chkMsg(this):
        """Read messages"""
        from temp_aber import readmsg, mstoout, update, eorte

        import world
        
        #~ extern long vdes,tdes,rdes;
        #~ extern FILE *fl_com;
        #~ extern long debug_mode;

        unit   = world.openw()
        fl_com = unit

        if not unit:
            raise Exception("AberMUD: FILE_ACCESS : Access failed")
            #~ Crapup

        lastMsg = world.findend(unit)
     
        if this.msgId == -1:
            this.msgId = lastMsg

        for i in range(this.msgId, lastMsg + 1):
            #~ WTF?
            block = ""
            readmsg(unit, block, i)
            mstoout(block, this.name)
            
        #~ WTF?
        update(this.name)
        eorte()

        #~ WTF?
        rdes = 0
        tdes = 0
        vdes = 0

    def special(this, string):
        """Special functions"""
        #~ Testing string
        s = string.lower()
        c = s[0]
        if c != '.':
            return False
        c = s[1]

        #~ Game start
        if c == 'g':
            this.gameStart()
        else:
            print("Unknown . option")

        return True

    def gameStart(this):
        """Starting command"""
        from temp_aber import initme, sendsys
        from temp_aber import my_str, my_lev, my_sex

        import world
        
        global mode

        mode  = 1
        initme()
            
        ufl = world.openw()
            
        if my_lev < 10000:
            vis = 0
        else:
            vis = 10000

        this.setStr(my_str)
        this.setLev(my_lev)
        this.setVis(vis)
        this.setWpn(-1)
        this.setSexAll(my_sex)
        this.setHlp(-1)
            
        xx = "\001s{0}\001[ {0}  has entered the game ]\n\001".format(this.name)
        sendsys(this.name, this.name, -10113, this.locId, xx)
            
        this.randLoc()
        this.chkMsg()

        xx = "\001s{0}\001{0}  has entered the game\n\001".format(this.name)
        sendsys(this.name, this.name, -10000, this.locId, xx)

    def randLoc(this):
        """Move user to random location"""
        from temp_aber import randperc, trapch

        if randperc() > 50:
            this.locId = -5
        else:
            this.locId = -183

        trapch(this.locId)

    def getName(this) :
        """Get user name"""
        return this.data[0]
       
    def getLoc(this) :
        """Get user location"""
        return this.data[4]
       
    def getPos(this) :
        """Get user position"""
        return this.data[5]
       
    def getStr(this) :
        """Get user strength"""
        return this.data[7]
       
    def getVis(this) :
        """Get user visibility"""
        return this.data[8]
       
    def getSexAll(this) :
        """Get user sex"""
        return this.data[9]
       
    def getSex(this) :
        """Get user sex"""
        return this.getSexAll() % 2
       
    def getLev(this) :
        """Get user level"""
        return this.data[10]
       
    def getWpn(this) :
        """Get user weapon"""
        return this.data[11]
       
    def getHlp(this) :
        """Get user helping"""
        return this.data[13]
       
    def setName(this, v) :
        """Set user name"""
        this.data[0] = v
       
    def setLoc(this, v) :
        """Set user location"""
        this.data[4] = v
       
    def setPos(this, v) :
        """Set user position"""
        this.data[5] = v
       
    def setStr(this, v) :
        """Set user strength"""
        this.data[7] = v
       
    def setVis(this, v) :
        """Set user visibility"""
        this.data[8] = v
       
    def setSexAll(this, v) :
        """Set user sex"""
        this.data[9] = v
       
    def setSex(this, v) :
        """Set user sex"""
        this.data[9] = v
        #~  &=
       
    def setLev(this, v) :
        """Set user level"""
        this.data[10] = v
       
    def setWpn(this, v) :
        """Set user weapon"""
        this.data[11] = v

    def setHlp(this, v) :
        """Set user helping"""
        this.data[13] = v

#~ char * pname(chr)
#~ ploc(chr)
#~ pchan(chr)
#~ pstr(chr)
#~ plev(chr)
#~ pvis(chr)
#~ psex(chr)
#~ psexall(chr)

#~ setplev(chr,v)
#~ setpstr(chr,v)
#~ setpvis(chr,v)
#~ setpsex(chr,v)
#~ setpsexall(chr,v)

mode = 0

def main():
    """User data"""
    print("User data and functions")
    return 0

if __name__ == '__main__':
    main()


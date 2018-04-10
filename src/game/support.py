'''

 Some more basic functions


 Note

 state(obj)
 setstate(obj,val)
 destroy(obj)

 are elsewhere

'''
# extern FILE* openlock();
# extern OBJECT objects[];

# ocarrf(ob)
# setocarrf(ob,v)
# oloc(ob)
# setoloc(ob,l,c)
# ploc(chr)
# char * pname(chr)
# plev(chr)
# setplev(chr,v)
# pchan(chr)
# pstr(chr)
# setpstr(chr,v)
# pvis(chr)
# setpvis(chr,v)
# psex(chr)
# setpsex(chr,v)
# setpsexall(chr,v)
# psexall(chr)
# char * oname(ob)
# char * olongt(ob,st)
# omaxstate(ob)
# obflannel(ob)  /* Old version */
# oflannel(ob)
# obaseval(ob)
# isdest(ob)
# isavl(ob)
# ospare(ob)
# ppos(chr)
# setppos(chr,v)
# setploc(chr,n)
# pwpn(chr)
# setpwpn(chr,n)
# ocreate(ob)


def syslog(*args):
    # tm = time()
    # z = ctime(tm)
    # z = ('\n' in z)=0;
    # x = openlock(LOG_FILE,"a")
    # if x is None:
        # loseme()
        # crapup("Log fault : Access Failure")
    # fprintf(x,"{}:  {}".format(z, args))
    # fclose(x);
    pass


# osetbit(ob,x)
# oclearbit(ob,x)
# oclrbit(ob,x)
# otstbit(ob,x)
# osetbyte(o,x,y)
# obyte(o,x)
# ohany(mask)
# long mask;
# phelping(x,y)
# setphelping(x,y)
# ptothlp(pl)
# psetflg(ch,x)
# long ch;
# pclrflg(ch,x)

# Pflags
#
# 0 sex
#
# 1 May not be exorcised ok
#
# 2 May change pflags ok
#
# 3 May use rmedit ok
#
# 4 May use debugmode ok
#
# 5 May use patch
#
# 6 May be snooped upon
#


# ptstbit(ch,x)
# ptstflg(ch,x)

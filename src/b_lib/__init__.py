'''
B functions and utilities
'''
#include <stdio.h>
#include <pwd.h>

#include <ctype.h>
#include "System.h"

# lowercase(str)
# uppercase(str)
# trim(str)
# any(ch,str)

def gepass(str):
    key = getpass("")
    pw = crypt(key, "XX")
    str = pw
    return pw


def scan(s_out, s_in, start, skips, stops):
    in_base = s_in
    # char *sy_ot=out;
	# printf("Scan(%s ->%d %d %s %s",in,out,start,skips,stops);
    if len(s_in) < start:
        s_out = 0
        return None
    s_in += start
    while s_in and strchr(skips, s_in):
        s_in++
	if s_in == 0:
        s_out = 0
        return None
    while s_in and strchr(stops, s_in) == 0:
        s_out = s_in
        s_out++
        s_in++
    # printf(" : Outputting %s\n",sy_ot);
    s_out = 0
    return (s_in - s_in_base)


def getstr(f, st):
    if not fgets(st, 255, f):
        return 0
    if strchr(st, '\n'):
        strchr(st, '\n') = 0
    return st


def addchar(str, ch):
    x += ch
    return x


def numarg(str):
    i = 0
    sscanf(str, " %ld", i)
    return i


def sbar():
    return None # Unknown code needed here


def f_listfl(name, f):
    a = fopen(name, "r")
    if a is None:
        fprintf(stderr, "[Cannot find file ->%s ]\n", name)
    else:
        while fgets(x, 127, a):
            fprintf(f, "%s", x)


def sec_read(unit, block, pos, l):
    fseek(unit, pos * 64 * sizeof(long), 0)
    fread(block, l * sizeof(long), 1, unit)


def sec_write(unit, block, pos, l):
    fseek(unit, pos * 64 * sizeof(long), 0)
    fwrite(block, l * sizeof(long), 1, unit)


def cuserid(str):
    # extern char *strchr();
	# getpw(getuid(),ary);
	# *strchr(ary,':')=0;
    ary = getpwuid(getuid()).pw_name
    if str is not None:
        str = ary
	return(ary)

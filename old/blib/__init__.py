#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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


# char *lowercase(str)
# char *uppercase(str)
# char *trim(str)
# long numarg(str)
# int any(ch,str)
# void gepass(str)


def scan(s, start, skips, stops):
    # sy_ot = out
    # print("Scan(%s -> %d %d %s %s)" % (s, out, start, skips, stops))

    if len(s) < start:
        return -1

    s = s[start:]
    out = ""
    status = 0
    for c in s:
        if (status == 0) and (c not in skips):
            status = 1
        if (status == 1) and (c in stops):
            break
        if status == 1:
            out = out + c

    # print(" : Outputting %s" % (sy_ot))
    return out


# char *getstr(file,st)
# FILE *file;
# char *st;
# {
# 	extern char *strchr();
# 	if(!fgets(st,255,file)) return(0);
# 	if(strchr(st,'\n')) *strchr(st,'\n')=0;
# 	return(st);
#  }

# void addchar(str,ch)
# char *str;
# char ch;
# {
# 	int x=strlen(str);
# 	str[x]=ch;
# 	str[x+1]=0;
# }


# sbar() Unknown code needed here

# void f_listfl(name,file)
# char *name;
#  FILE *file;
# {
# 	FILE *a;
# 	char x[128];
# 	a=fopen(name,"r");
# 	if(a==NULL) fprintf(stderr,"[Cannot find file ->%s ]\n",name);
# 	else
#       {
# 	while(fgets(x,127,a)) fprintf(file,"%s",x);
#        }
# }

# void sec_read(unit,block,pos,len)
# FILE *unit;
# long *block;
# long pos;
# long len;
# {
# 	fseek(unit,pos*64*sizeof(long),0);
# 	fread((char *)block,len*(sizeof(long)),1,unit);
#       print("TODO: sec_read(%s, %s, %d, %d)" % (f, data, begin, end))
# }

def sec_write(unit, block, pos, len):
    c = 64
    l = 4
    # print("TODO: Write to %s" % (unit))
    # print("TODO: Seek for %s from start" % (pos * c * l))
    # print("TODO: Write 1 element of %d from %s" % (len*l, block))

    import json
    unit.write("Search %d\n" % (pos*c*l))
    unit.write("Size %d\n" % (len*l))
    unit.write(json.dumps(block))
    unit.write("\n")

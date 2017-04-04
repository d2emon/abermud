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


ttyt = 0

qnmrq = False

def clear_console():
    print('-=' * 80)


def crapup(msg):
    import sys

    clear_console()
    input("\n%s\n\nHit Return to Continue...\n" % (msg))
    sys.exit(1)


def elapsed(delta):
    """
    Elapsed time and similar goodies
    """
    if delta.days > 1:
        return "Over a day!!!"

    parts = []
    hour = 60 * 60
    hours = delta.seconds // hour
    seconds = delta.seconds % hour
    minutes = seconds // (60)

    if hours > 1:
        parts.append("%d hours" % (hours))
    elif hours == 1:
        parts.append("1 hour")

    if minutes > 1:
        parts.append("%d minutes" % (minutes))
        return " and ".join(parts)
    elif minutes == 1:
        parts.append("1 minute")

    seconds = (delta.seconds % 60)
    if seconds > 1:
        parts.append("%d seconds" % (seconds))
    elif seconds == 1:
        parts.append("1 second")

    return " and ".join(parts)

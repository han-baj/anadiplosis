#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ANADIPLOSIS FINDER - Searches a text file for longest possible chain of anadiploses
#

import re
import sys
import itertools
file = "/Users/hannesbajohr/Dropbox/SCRIPTS/PYTHON/Anadiplosis/wagnerpopp_scramble.txt"
with open(file) as g:
    all_lines = g.readlines()

def last_word(particular_line):
    if particular_line != "\n": 
        particular_line = re.sub(ur'^\W*|\W*$', "",particular_line)
        if len(particular_line) > 1:
            return particular_line.rsplit(None, 1)[-1].lower()

def first_word(particular_line):
    if particular_line != "\n": 
        particular_line = re.sub(ur'^\W*|\W*$', "",particular_line) 
        if len(particular_line) > 1:
            return particular_line.split(None, 1)[0].lower()

def chain(start, lines, depth):
    remaining = list(lines) 
    del remaining[remaining.index(start)]
    possibles = [x for x in remaining if (len(x.split()) > 2) and (first_word(x) == last_word(start))]
    maxchain = []
    for c in possibles:
        l = chain(c, remaining, depth)
        sys.stdout.flush()
        sys.stdout.write(str(depth) + " of " + str(len(all_lines)) + "   \r")
        sys.stdout.flush()
        if len(l) > len(maxchain):
            maxchain = l
            depth = str(depth) + "." + str(len(maxchain))
    return [start] + maxchain

#Start
final_output = []

#Finding the longest chain of anadiploses

for i in range (0, len(all_lines)):
    x = chain(all_lines[i], all_lines, i)
    if len(x) > 2:  
        final_output.append(x)
        print x
final_output.sort(key = len)

#Output on screen
print "\n\n--------------------------------------------"

if len(final_output) > 1: 
    print "\n".join(final_output[-1])
else: 
    print "Nothing found"
#!/usr/bin/python

import sys
file = open(sys.argv[1], "r")

def shift(c, d):
    if "A"<=c<="Z": k = 65
    elif "a"<=c<="z": k = 97
    else: return c
    l = k+25
    n = ord(c)
    r = n+d
    while r>l: r-=25
    while r<k: r+=25
    return chr(r)
    
d = int(file.readline()[:-1])
for st in file:
    print "".join(map((lambda x:shift(x,d)), st[:-1]))

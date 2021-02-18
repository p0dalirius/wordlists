#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import sys

def readfile(file, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "r"+b_opt)
    data = f.readlines()
    f.close()
    return data

def writefile(file, data, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "w"+b_opt)
    for e in data:
        f.write(e)
    f.close()
    return data

def prime_factors(n):
    factors = []
    for k in range(2,n+2):
        while n % k == 0:
            factors.append(k)
            n = n//k
    return factors

LOGFREQUENCY=1000

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage : python3 "+sys.argv[0]+" outfile MAXI")
    else :
        outfile = sys.argv[1]
        maxi = int(sys.argv[2])
        open(outfile, "w").close() # Create the file
        for n in range(3, maxi, 2):
            if (n+1) % (maxi//LOGFREQUENCY) == 0 :
                print("\r\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m Currently at "+str(round(((n+1)/(maxi))*100, 2))+" %  ", end="")
            line = str(n)+" : "+",".join([str(e) for e in prime_factors(n)])
            f = open(outfile, "a")
            f.write(line+"\n")
            f.close()
        print()

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

def factorial(number):
    factorial = 1
    for num in range(number,1,-1):
        factorial = factorial * num
    return factorial

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
            f = open(outfile, "a")
            f.write(str(factorial(n))+"\n")
            f.close()
        print()

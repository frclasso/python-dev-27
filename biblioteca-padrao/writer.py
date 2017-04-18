#!/usr/bin/python

import sys

temp = open('temp.txt', 'w')

for i in range(100):
    temp.write('%03d\n'% i)

temp.close()
temp = open('temp.txt')

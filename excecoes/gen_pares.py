#!/usr/bin/python

#coding: utf-8

def gen_pares():
    i = 0
    while True:
        i += 2
        yield i

for n in gen_pares():
    print n

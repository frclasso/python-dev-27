#!/usr/bin/python

"""reading a csv file"""
import csv

dt = csv.reader(file('dt.csv'))

for reg in dt:
    print reg	

#!/usr/bin/python

import csv

dt = (('temperatura',15.0, 'C','10:40', '2006-12-31'), ('peso',42.5, 'Kg', '10:45', '2006-12-31'))
out = csv.writer(file('dt.csv', 'w'))
out.writerows(dt)

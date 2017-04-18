#!/usr/bin/python

#coding: utf-8

import pickle

try:
	setup = pickle.load(file('setup.pkl'))
	print setup
except:
	setup = {'timeout':10,
	         'server':'10.0.0.1',
	         'port':80
	         }
	pickle.dump(setup, file('setup.pkl', 'w'))
#!/usr/bin/python
# -*-coding: utf-8 -*-
import sys
from subprocess import PIPE, Popen

cmd = 'ping -c 4'
if sys.platform == 'win32':
    cmd = 'ping -n 4'

host = '8.8.8.8'

"""Comunicacao com outro processo, 
um pipe com stdout do comando """

py = Popen(cmd + host, stdout=PIPE)
print (py.stdout.read())

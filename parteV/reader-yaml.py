#!/usr/bin/python

import pprint
import yaml

yml = yaml.load(file('prefs.yaml'))
pprint.pprint(yml)

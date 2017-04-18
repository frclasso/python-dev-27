#!/usr/bin/python

#coding: utf-8

import yaml

progs = {
        'Inglaterra':
             {
              'Yes':['Close to the Edge', 'Fragile'],
              'Genesis':['Foxtrot','The Nursey Crime'],
              'King Crimson':['Red','Discipline']},
        'Alemanha':
            {'Kraftwerk':['Radioactivity', 'Trans Europe Express']}
        }
print yaml.dump(progs)

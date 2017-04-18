#!/usr/bin/python

#-*-coding: utf-8 -*-
"""modutils - rotinas utilitarias para modulos
"""

import os.path, sys, glob

def find(txt):
    """encontra  modulos que tem o nome contendo o paramentro"""

    resp = []
    for path in sys.path:
        mods = glob.glob('%s/*.py'% path)
        for mod in mods:
            if txt in os.path.basename(mod):
                resp.append(mod)
    return resp

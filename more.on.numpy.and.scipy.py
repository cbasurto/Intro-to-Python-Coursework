# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 09:47:47 2015

@author: ESAccount18
"""

import time
import numpy

def trad_version():
    t1 = time.time()
    x = range(10000000)
    y = range(10000000)
    z = []
    for i in range(len(x)):
        z.append(x[i] + y[i])
        return time.time() - t1

def numpy_version():
    t1 = time.time()
    x = numpy.arange(10000000)
    y = numpy.arange(10000000)
    z = x + y
    return time.time() - t1
    
print trad_version()
print numpy_version()

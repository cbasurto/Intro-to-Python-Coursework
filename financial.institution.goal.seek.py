# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:51:43 2015

@author: ESAccount24
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:34:21 2015

@author: ESAccount24
"""
#financial institutions
import numpy as np
import scipy.optimize as sp
def myfnc(x):
    return np.pv(x,2,0,125.44)+100.0
    
futval=np.fv(0.12,2,0,-100.0)
print futval
prval=np.pv(0.12,2,0,125.44)
print prval

nperiods=np.nper(0.12,0,-100.0,125.44)
print nperiods

intrate=np.rate(2,0,-100,125.44)
print intrate

initialRateGuess=0.134

#goalseek
#find interest rate that satisfies euqation connecting pv, fv, and nper
print sp.fsolve(myfnc,initialRateGuess)
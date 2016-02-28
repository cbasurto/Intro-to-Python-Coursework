# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:45:49 2015

@author: ESAccount24
"""

_str = 'X-DSPAM-Confidence:0.8475'
host = float(_str.split(':')[1])
print(host)
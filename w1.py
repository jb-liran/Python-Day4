# -*- coding: utf-8 -*-
"""
Created on Tue May  8 12:09:13 2018

@author: jbt
"""

import warnings
 
def fn(a):
    s=0;
    if a>100:
        warnings.warn('Long Wait...')
    for i in range(a):
        s+=i
    return s


warnings.filterwarnings('error','.*') 
print("Start...")
print(fn(1000))
print ("Ending...")
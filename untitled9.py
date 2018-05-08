# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:09:08 2018

@author: jbt
"""

from threading import Thread
import time

def myfunc1(*args):
    n=50
    while n>0:
        n-=1
        print ("From thread", args)
        time.sleep(1)
        
def myfunc2(*args):
    n=12
    while n>0:
        n-=1
        print ("From thread", args)
        time.sleep(2)
   
th1 = Thread(target=myfunc1, args='T1')
th2 = Thread(target=myfunc2, args='T2')
th1.start()
th2.start()
print ("From main")
#th1.join()
#th2.join()
print ("end main")

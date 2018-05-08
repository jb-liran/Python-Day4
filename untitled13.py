# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:53:40 2018

@author: jbt
"""

import threading
import time
 
lc = threading.Lock()
 
 
def myfunc1(*args):
    global lc
    lc.acquire()
    
    print("From thread 1111", args)
    time.sleep(3)
    print("From thread 1111", args)
    
    lc.release()
 
def myfunc2(*args):
    global lc
    lc.acquire()
    
    print("From thread 2222", args)
    time.sleep(3)
    print("From thread 2222", args)
    
    lc.release()
 
 
tid1 = threading.Thread(target=myfunc1, args='T1')
tid2 = threading.Thread(target=myfunc2, args='T2')
tid1.start()
tid2.start()
print("From main")
tid1.join()
tid2.join()
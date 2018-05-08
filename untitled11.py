# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:33:27 2018

@author: jbt
"""

import threading
import time

class MyThread (threading.Thread):
    def __init__(self,a,b):
        threading.Thread.__init__(self)
        self.__a = a
        self.__b = b
    def run (self):
        for i in range(5):
            print ("In thread", self.name, self.__a + self.__b)
            time.sleep(2)
 
th1 = MyThread(10,30)
th2 = MyThread(20,350)
th1.setName("t1")
th2.setName("t2")
th1.start()
th2.start()
print ("From main")
th1.join()
th2.join()